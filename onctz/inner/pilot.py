"""from onctz.inner.browser import Browser
from onctz.services.facebook import Facebook
from onctz.services.google import Google
from onctz.services.arisp import Arisp
from onctz.services.sivec import Sivec
from onctz.services.siel import Siel
from onctz.services.jucesp import Jucesp
from onctz.services.infoseg import Infoseg
from onctz.services.caged import Caged


facebook = Facebook(browser)
v_google = Google(browser)
# v_sivec = Sivec(browser)
v_infoseg = Infoseg(browser)
# v_siel = Siel(browser)
v_jucesp = Jucesp(browser)
v_caged = Caged(browser)


def logins():
    # browser = navigator()
    browser.navigate('https://facebook.com')
    facebook.login('fiapm1spear@gmail.com', 'geckoChrome')
    return


def fbook(person_name):
    facebook.navigate('https://facebook.com')
    facebook.search_person(person_name)
    facebook.get_search_results()
    # facebook.get_all_profiles()
    # browser.quit()


def navigator(url):
    browser.navigate(url)


def google(person_name):
    browser.navigate('http://google.com.br')
    v_google.search(person_name)
    print(v_google.get_results())


def arisp(cpf_cnpj):
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/arisp/login.html')
    v_arisp.search(cpf_cnpj)
    v_arisp.get_results()


def sivec_nome(nome):
    v_sivec = Sivec(browser)
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/sivec/login.html')
    v_sivec.login('login', 'senha')
    v_sivec.search_nome(nome)
    v_sivec.get_results_nome()


def sivec_sap(matriculaSap):
    v_sivec = Sivec(browser)
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/sivec/login.html')
    v_sivec.login('login', 'senha')
    v_sivec.search_sap(matriculaSap)
    v_sivec.get_results_sap()


)


def siel(brw, nome, numProcesso):
    brw = navigator()
    v_siel = Siel(brw)
    brw.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/siel/login.html')
    v_siel.login('login', 'senha')
    v_siel.search(nome, numProcesso)
    v_siel.get_results()


def jucesp(nomeEmp):
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/jucesp/index.html')
    v_jucesp.search(nomeEmp)
    v_jucesp.get_results()



def detran_cnh(cpf):
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/detran/login.html')
    v_detran.login('login', 'senha')
    v_detran.get_search_cnh(cpf)
    v_detran.get_results_cnh()


def infoseg(cpf):
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/infoseg/login.html')
    v_infoseg.login('login', 'senha')
    v_infoseg.search(cpf)
    v_infoseg.get_results()


def caged_responsavel(chave):
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/caged/login.html')
    v_caged.login('login', 'senha')
    v_caged.search_responsavel(chave)
    v_caged.get_results_responsavel()


def caged_empresa(cnpj):
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/caged/login.html')
    v_caged.login('login', 'senha')
    v_caged.search_emp(cnpj)
    v_caged.get_results_emp()


def caged_trabalhador(chave):
    browser.navigate('http://ec2-18-231-116-58.sa-east-1.compute.amazonaws.com/caged/login.html')
    v_caged.login('login', 'senha')
    v_caged.search_trab(chave)
    v_caged.get_results_trab()


def close_all_tabs():
    for i in range(len(browser.window_handles)):
        browser.close()
"""
