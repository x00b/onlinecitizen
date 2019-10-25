from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import onctz.api.model.models as modeller



class Cadesp:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.cadesp_data = None
        self.Model = model

    def login(self, login, password):
        self.driver.find_element_by_id('ctl00_conteudoPaginaPlaceHolder_loginControl_UserName').send_keys(login)
        self.driver.find_element_by_id('ctl00_conteudoPaginaPlaceHolder_loginControl_Password').send_keys(password)
        self.driver.find_element_by_name('ctl00$conteudoPaginaPlaceHolder$loginControl$loginButton').click()

    def search(self, cnpj):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//tbody/tr/td/a[@href='https://www.cadesp.fazenda.sp.gov.br/(S(wyminl552cyomgasm4yfb245))/Pages/Principal.aspx#']")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//tbody/tr/td/a[@href='pagina3-pesquisa.html']").click()
        self.driver.find_element_by_name("ctl00$conteudoPaginaPlaceHolder$tcConsultaCompleta$TabPanel1$lstIdentificacao").click()
        self.driver.find_element_by_xpath("//select[@name='ctl00$conteudoPaginaPlaceHolder$tcConsultaCompleta$TabPanel1$lstIdentificacao']/option[@value='2']").click()
        self.driver.find_element_by_name("ctl00$conteudoPaginaPlaceHolder$tcConsultaCompleta$TabPanel1$txtIdentificacao").send_keys(cnpj)
        self.driver.find_element_by_name("ctl00$conteudoPaginaPlaceHolder$tcConsultaCompleta$TabPanel1$btnConsultarEstabelecimento").click()

    def get_results(self):
        ie = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[2]/td[2]").text
        cnpj = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[3]/td[2]").text
        nomeEmpresarial = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[4]/td[2]").text
        drt = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[5]/td[2]").text
        auxsituacao = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[2]/td[3]").text.split("Situação:")
        auxdataInscricaoEstado = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[3]/td[3]").text.split("Data da Inscrição no Estado:")
        auxregimeEstadual = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[4]/td[3]").text.split("Regime Estadual:")
        auxpostoFiscal = self.driver.find_element_by_xpath("//*[@id='ctl00_conteudoPaginaPlaceHolder_dlCabecalho']/tbody/tr/td/table/tbody/tr[5]/td[3]").text.split("Posto Fiscal:")
        situacao = auxsituacao[1]
        dataInscricaoEstado = auxdataInscricaoEstado[1]
        regimeEstadual = auxregimeEstadual[1]
        postoFiscal = auxpostoFiscal[1]

        self.cadesp_data = modeller.Cadesp(ie, cnpj, nomeEmpresarial, drt, situacao, dataInscricaoEstado, regimeEstadual, postoFiscal, self.Model.search_hash)
        self.driver.quit()
        return self.cadesp_data
