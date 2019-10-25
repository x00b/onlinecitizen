from flask import request, jsonify, Response
from onctz.api.gen_passwd import Hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token
)
from json import dumps
from onctz.api.model.models import *
from onctz.metadata import conf, pilot
from onctz.api.util import Util
from uuid import uuid1
from onctz.orchestrator import Orchestrator
import datetime
import pytz

app = conf.app
db = conf.db
ma = conf.ma
jwt = JWTManager(conf.app)

user_schema = UserSchema()
search_schema = SearchSchema()
searchs_schema = SearchSchema(many=True)


@app.route('/init', methods=['GET'])
def init():
    try:
        db.create_all()
        return 'OK', 200
    except Exception:
        return 'Not OK', 400


@app.route('/newuser', methods=['POST'])
def new_user():
    newuser = User(request.json['username'], Hash.hash_password(request.json['password']))
    try:
        db.session.add(newuser)
        db.session.commit()
        return user_schema.jsonify(newuser), 201
    except Exception:
        return "Try other username", 418


@app.route('/login', methods=['POST'])
def session():
    username = request.json['username']
    password = request.json['pass']
    user = db.session.query(User.username, User.password).filter_by(username=username).first()
    try:
        if Hash.verify_password(user[1], password):
            access_token = create_access_token(identity=username)
            return dumps({'access_token': access_token}), 201
        else:
            return "invalid", 200
    except Exception:
        return "invalid", 200


@app.route('/auth', methods=['POST'])
def auth():
    username = request.json['username']
    hash = request.json['search_hash']

    try:
        user_id = db.session.query(User.user_id).filter_by(username=username).first()[0]
        searcher_user = db.session.query(Search.by_user).filter_by(search_hash=hash).first()[0]
        if searcher_user == user_id:
            return jsonify({'valid': 1}), 200
        else:
            raise Exception("Invalid")
    except Exception:
        return jsonify({'valid': 0}), 401


def search_exec(services, search_hash):
    orq = Orchestrator()
    orq.define_services(services, search_hash)
    orq.conclude()
    conf.engine.update_status(search_hash)


@app.route('/search', methods=['POST'])
def search():
    services = Util().check_json(request.get_json())
    search_hash = Hash.hash_password(str(uuid1()))
    username = request.get_json().get('username')
    alias = request.get_json().get('alias')

    try:
        user_id = db.session.query(User.user_id).filter_by(username=username).first()
        date = datetime.datetime.now(pytz.timezone('Brazil/East')).strftime("%d/%m/%Y %I:%M%p")
        newsearch = Search(search_hash, alias, 0, date, user_id[0])
        db.session.add(newsearch)
        db.session.commit()
    except Exception:
        return 'User invalid', 500

    conf.queue.enqueue(search_exec, args=(services, search_hash,))

    return search_schema.jsonify(newsearch), 201


@app.route('/searches', methods=['GET', 'POST'])
def get_search():
    username = request.get_json().get('username')
    try:
        user_id = db.session.query(User.user_id).filter_by(username=username).first()[0]
    except Exception:
        return 'User invalid', 500
    search = Search.query.filter_by(by_user=user_id)[::-1]
    return searchs_schema.jsonify(search), 200


@app.route('/gethash/<hash>', methods=['GET'])
def get_hash(hash):
    try:
        data = Util().format_export(hash)
        return jsonify(data), 200
    except Exception:
        return '', 204


@app.route('/getreport/<hash>', methods=['GET'])
def get_report(hash):
    report = conf.engine.generate_report(hash, pilot.services_template, pilot.services_list, pilot.relatorio)
    return report, 200


@app.route('/delete', methods=['POST'])
def delete():
    try:
        hash = request.get_json().get('search_hash')
        # search = Search.query.filter(search_hash=hash).one()
        search = db.session.query(Search).filter_by(search_hash=hash).first()
        db.session.delete(search)
        db.session.commit()
        return '', 202
    except:
        return '', 418


def run_api():
    app.run(debug=True)
