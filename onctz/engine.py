from onctz.inner.browser import Browser
from onctz.services.arisp import Arisp
from onctz.services.arpenp import Arpenp
from onctz.services.cadesp import Cadesp
from onctz.services.censec import Censec
from onctz.services.detran import Detran
from onctz.services.infocrim import Infocrim
from onctz.services.caged import Caged
from onctz.services.jucesp import Jucesp
from onctz.services.siel import Siel
from onctz.services.sivec import Sivec

from onctz.api.model.DAO import Model
import onctz.api.model.models as modeller
from onctz.api.util import Util


class Engine:
    def __init__(self, conf=None):
        self.conf = conf

    def newinstance(self):
        self.browser = Browser()
        self.browser.driver_path = "./onctz/inner/drivers/chromedriver"
        self.browser.setup('chrome')
        return self.browser

    def appinstance(self, app):
        self.app = app

    def dbsession(self, db):
        self.db = db

    def mainstance(self, ma):
        self.ma = ma

    def generate_report(self, hash, templates, service_list, relatorio):
        data = Util().format_export(hash)
        report = relatorio.format(search_hash=hash[:40])
        aux = ""
        for i in range(len(service_list)):
            if data[service_list[i]] is not None:
                try:
                    aux = aux + templates[i].format(**data[service_list[i]])
                except:
                    pass
        response = report + aux + " </div>\n   </div>\n  </body>\n</html>"
        return response

    def update_status(self, search_hash):
        search = modeller.Search.query.filter_by(search_hash=search_hash).first()
        search.status = 1
        self.db.commit()

    def arisp_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        arisp = pilot.service.arisp(target)
        self.db.add(arisp)
        self.db.commit()

    def arpenp_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        arpenp = pilot.service.arpenp(target)
        self.db.add(arpenp)
        self.db.commit()

    def cadesp_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        cadesp = pilot.service.cadesp(target)
        self.db.add(cadesp)
        self.db.commit()

    def cagedresp_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        cagedresp = pilot.service.caged_responsavel(target)
        self.db.add(cagedresp)
        self.db.commit()

    def cagedtrab_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        cagedtrab = pilot.service.caged_trabalhador(target)
        self.db.add(cagedtrab)
        self.db.commit()

    def cagedemp_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        cagedemp = pilot.service.caged_empresa(target)
        self.db.add(cagedemp)
        self.db.commit()

    def censec_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        censec = pilot.service.censec(target)
        self.db.add(censec)
        self.db.commit()

    def detrancnh_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        detrancnh = pilot.service.detran_cnh(target)
        self.db.add(detrancnh)
        self.db.commit()

    def infocrim_search(self, pilot, search_hash):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        infocrim = pilot.service.infocrim()
        self.db.add(infocrim)
        self.db.commit()

    def jucesp_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        jucesp = pilot.service.jucesp(target)
        self.db.add(jucesp)
        self.db.commit()

    def siel_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        siel = pilot.service.siel(target)
        self.db.add(siel)
        self.db.commit()

    def sivecnome_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        sivec = pilot.service.sivec_nome(target)
        self.db.add(sivec)
        self.db.commit()

    def sivecsap_search(self, pilot, search_hash, target):
        brw = self.newinstance()
        pilot.search(brw)
        pilot.service.setModel(search_hash)
        sivecsap = pilot.service.sivec_sap(target)
        self.db.add(sivecsap)
        self.db.commit()


class Service:
    def __init__(self, browser):
        self.browser = browser
        self.model = None

    def setModel(self, hash):
        self.model = Model(hash)

    def arisp(self, cpf_cnpj):
        v_arisp = Arisp(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/arisp/login.html')
        try:
            v_arisp.search(cpf_cnpj)
            v_arisp.get_results()
            return v_arisp.arisp_data
        except:
            return modeller.Arisp("error", self.model.search_hash)

    def arpenp(self, numProcesso):
        v_arpenp = Arpenp(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/arpensp/login.html')
        # add try/except =>
        try:
            v_arpenp.search(numProcesso)
            return v_arpenp.get_results()
        except Exception:
            return modeller.Arpenp("error", "error", "error", "error", "error", "error", "error", "error", "error", "error", "error", self.model.search_hash)

    def cadesp(self, cnpj):
        v_cadesp = Cadesp(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/cadesp/login.html')
        try:
            v_cadesp.login('fiap', 'mpsp')
            v_cadesp.search(cnpj)
            return v_cadesp.get_results()
        except:
            return modeller.Cadesp("error", "error", "error", "error", "error", "error", "error", "error", self.model.search_hash)

    def caged_responsavel(self, chave):
        v_caged = Caged(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/caged/login.html')
        try:
            v_caged.login('login', 'senha')
            v_caged.search_responsavel(chave)
            v_caged.get_results_responsavel()
            return v_caged.cagedresponsavel_data
        except:
            return modeller.CagedResponsavel("error", "error", "error",  "error", "error", "error", "error", "error", "error", "error", self.model.search_hash)

    def caged_trabalhador(self, chave):
        v_caged = Caged(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/caged/login.html')
        try:
            v_caged.login('login', 'senha')
            v_caged.search_trab(chave)
            v_caged.get_results_trab()
            return v_caged.cagedtrabalhador_data
        except:
            return modeller.CagedTrabalhador("error", "error", "error", "error", "error", "error", "error", "error", "error", "error", "error", "error", "error", self.model.search_hash)

    def caged_empresa(self, chave):
        v_caged = Caged(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/caged/login.html')
        try:
            v_caged.login('login', 'senha')
            v_caged.search_emp(chave)
            v_caged.get_results_emp()
            return v_caged.cagedempresa_data
        except:
            return modeller.CagedEmpresa("error", "error", "error", "error", "error", "error", self.model.search_hash)

    def censec(self, cpf_cnpj):
        v_censec = Censec(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/censec/login.html')
        try:
            v_censec.login('login', 'senha')
            v_censec.search(cpf_cnpj)
            v_censec.get_results()
            return v_censec.censec_data
        except:
            return modeller.Censec("error", "error", "error", "error", "error", self.model.search_hash)

    def detran_cnh(self, cpf):
        v_detran = Detran(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/detran/login.html')
        try:
            v_detran.login('login', 'senha')
            v_detran.get_search_cnh(cpf)
            v_detran.get_results_cnh()
            return v_detran.detrancnh_data
        except:
            return modeller.DetranCnh("error", "error", "error", "error", "error", "error", "error", "error", "error", "error", "error", self.model.search_hash)

    def infocrim(self):
        v_infocrim = Infocrim(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/infocrim/login.html')
        try:
            v_infocrim.login('login', 'senha')
            v_infocrim.search()
            return v_infocrim.get_results()
        except:
            return modeller.Infocrim("error", self.model.search_hash)

    def jucesp(self, nome):
        v_jucesp = Jucesp(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/jucesp/index.html')
        v_jucesp.search(nome)
        return v_jucesp.get_results()

    def siel(self, nome):
        v_siel = Siel(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/siel/login.html')
        v_siel.login('login', 'senha')
        v_siel.search(nome, "321")
        v_siel.get_results()
        return v_siel.sieldata

    def sivec_nome(self, nome):
        v_sivec = Sivec(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/sivec/login.html')
        v_sivec.login('login', 'senha')
        v_sivec.search_nome(nome)
        v_sivec.get_results_nome()
        return v_sivec.sivecnome_data

    def sivec_sap(self, sap):
        v_sivec = Sivec(self.browser, self.model)
        self.browser.navigate('http://fiap:mpsp@ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/sivec/login.html')
        v_sivec.login('login', 'senha')
        v_sivec.search_sap(sap)
        v_sivec.get_results_sap()
        return v_sivec.sivecsap_data
