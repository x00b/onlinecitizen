from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import path
from onctz.api.gen_passwd import Hash
from onctz.engine import Engine, Service
import redis
from rq import Queue


class Metadata:

    # flask app, sqlalchemy and marshmallow setup
    app = Flask(str("oncitizen"))
    basedir = path.abspath(path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'onctz.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = Hash.hash_password('asee((n][]@@ìi*&$%@kal')
    app.config['JSON_AS_ASCII'] = False
    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379',
        CELERY_RESULT_BACKEND='redis://localhost:6379'
    )
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    rds = redis.Redis()
    queue = Queue(connection=rds)

    def __init__(self):
        self.engine = None
        self.MetadataEngine()

    def MetadataEngine(self):
        # create a new engine instance for the runtime
        self.engine = Engine()
        self.engine.appinstance(self.app)
        self.engine.dbsession(self.db.session)
        self.engine.mainstance(self.ma)


class Pilot:
    services_list = {
        0: 'arpenp',
        1: 'cadesp',
        2: 'caged_resp',
        3: 'caged_trab',
        4: 'caged_emp',
        5: 'censec',
        6: 'detran_cnh',
        7: 'infocrim',
        8: 'jucesp'
    }

    relatorio = ("<!DOCTYPE html>\n"
                 "  <head>\n"
                 "    <title>Report - Template</title>\n"
                 "    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.css\">\n"
                 "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
                 "    <meta charset=\"UTF-8\">\n"
                 "    <script defer src=\"https://use.fontawesome.com/releases/v5.3.1/js/all.js\"></script>\n"
                 "  </head>\n"
                 "\n"
                 "  <body>\n"
                 "    <div class=\"container\">\n"
                 "      <div class=\"card\">\n"
                 "        <div class=\"card-content media-left\">\n"
                 "            <h2 class=\"title is-2\">OnCtz - Report</h2>\n"
                 "        </div>\n"
                 "      </div><br>\n"
                 "     <div>\n"
                 "       <b>Search Hash: </b>\n"
                 "       <span class=\"tag is-dark\" style=\"font-size: 0.4\">{search_hash}</span>\n"
                 "     </div>\n"
                 "     <hr>\n"
                 "     <div class=\"container\" style=\"float: left\">\n"
                 "    ")

    services_template = {
        0: (" \n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Arpenp</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>Registro cartório: {cartorioRegistro}</li>\n"
            "            <li>Numero CNS: {numeroCns}</li>\n"
            "            <li>UF: {uf}</li>\n"
            "            <li>Nome Conjuge1: {nomeConjuge1}</li>\n"
            "            <li>Novo Nome Conjuge1: {novoNomeConjuge1}</li>\n"
            "            <li>Nome Conjuge2: {nomeConjuge2}</li>\n"
            "            <li>Novo Nome Conjuge2: {novoNomeConjuge2}</li>\n"
            "            <li>Data Casamento: {dataCasamento}</li>\n"
            "            <li>Data Entrada: {dataEntrada}</li>\n"
            "            <li>Data Registro: {dataRegistro}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>"),
        1: ("\n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Cadesp</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>IE: {ie}</li>\n"
            "            <li>CNPJ: {cnpj}</li>\n"
            "            <li>Nome Empresarial: {nomeEmpresarial}</li>\n"
            "            <li>DRT: {drt}</li>\n"
            "            <li>Situação: {situacao}</li>\n"
            "            <li>Data Inscrição: {dataInscricaoEstado}</li>\n"
            "            <li>Regime Estadual: {regimeEstadual}</li>\n"
            "            <li>Posto Fiscal: {postoFiscal}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>\n"
            "        "),
        2: ("\n"
            "              <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Caged Responsável</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>CPF/CNPJ: {cnpj_cpf}</li>\n"
            "            <li>Logradouro: {logradouro}</li>\n"
            "            <li>Bairro: {bairro}</li>\n"
            "            <li>Municipio: {municipio}</li>\n"
            "            <li>UF: {uf}</li>\n"
            "            <li>CEP: {cep}</li>\n"
            "            <li>Nome: {nome}</li>\n"
            "            <li>CPF: {cpf}</li>\n"
            "            <li>Telefone: {telefone}</li>\n"
            "            <li>Email: {email}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>"),
        3: ("\n"
            "              <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Caged Trabalhador</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>Nome: {nome}</li>\n"
            "            <li>Pis base: {pis_base}</li>\n"
            "            <li>  Convertido: {pis_convertido}</li>\n"
            "            <li>CPF: {cpf}</li>\n"
            "            <li>CTPS: {ctps}</li>\n"
            "            <li>Situacao Pis: {situacao_pis}</li>\n"
            "            <li>Nacionalidade: {nacionalidade}</li>\n"
            "            <li>Grau Instrucao: {grau_instrucao}</li>\n"
            "            <li>Deficiente: {pessoa_deficiencia}</li>\n"
            "            <li>Nascimento: {nascimento}</li>\n"
            "            <li>UF CTPS: {uf_ctps}</li>\n"
            "            <li>Sexo: {sexo}</li>\n"
            "            <li>Raca: {raca}</li>\n"
            "            <li>CEP: {cep}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>"),
        4: ("\n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Caged Empresa</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>CNPJ: {cnpj}</li>\n"
            "            <li>Razao Social: {razao_social}</li>\n"
            "            <li>CNAE: {cnae}</li>\n"
            "            <li>Numero Filiais: {numero_filiais}</li>\n"
            "            <li>Vinculos: {total_vinculos}</li>\n"
            "            <li>Desligamentos: {desligamentos}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>"),
        5: ("\n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Censec</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>Carga: {carga}</li>\n"
            "            <li>Data: {data}</li>\n"
            "            <li>Ato: {ato}</li>\n"
            "            <li>Data Ato: {data_ato}</li>\n"
            "            <li>Partes: {partes}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>"),
        6: ("\n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>DetranCNH</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "                <ul>\n"
            "                <li>Renach: {renach}</li>\n"
            "                <li>Categoria: {categoria}</li>\n"
            "                <li>Emissao: {emissao}</li>\n"
            "                <li>Data Nascimento: {nascimento}</li>\n"
            "                <li>Nome: {nome}</li>\n"
            "                <li>Identidade: {identidade}</li>\n"
            "                <li>CPF: {cpf}</li>\n"
            "                <li>Nome mãe: {nome_mae}</li>\n"
            "                <li>Nome Pai: {nome_pai}</li>\n"
            "                <li>Registro: {registro}</li>\n"
            "                <li>Tipografico: {tipografico}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>"),
        7: ("\n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Infocrim</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "          <ul>\n"
            "            <li>Relatorio: {relatorio}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>"),
        8: ("\n"
            "        <article class=\"message\">\n"
            "        <div class=\"message-header\">\n"
            "          <p>Jucesp</p>\n"
            "        </div>\n"
            "        <div class=\"message-body\">\n"
            "                <ul>\n"
            "                <li>Nome Emp: {nome_emp}</li>\n"
            "                <li>Tipo Emp: {tipo_emp}</li>\n"
            "                <li>Data Constituição: {data_constituicao}</li>\n"
            "                <li>Data Inicio Atividade: {data_inicio_atividade}</li>\n"
            "                <li>CNPJ: {cnpj}</li>\n"
            "                <li>Inscrição estadual: {inscricao_estadual}</li>\n"
            "                <li>Objeto: {objeto}</li>\n"
            "                <li>Capital: {capital}</li>\n"
            "                <li>Logradouro: {logradouro}</li>\n"
            "                <li>Bairro: {bairro}</li>\n"
            "                <li>Municipio: {municipio}</li>\n"
            "                <li>Número: {numero}</li>\n"
            "                <li>Complemento: {complemento}</li>\n"
            "                <li>CEP: {cep}</li>\n"
            "                <li>UF: {uf}</li>\n"
            "          </ul>\n"
            "        </div>\n"
            "      </article>")
        }

    def search(self, browser):
        self.service = Service(browser)


pilot = Pilot()
conf = Metadata()
