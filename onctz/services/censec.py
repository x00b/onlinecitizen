from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import onctz.api.model.models as modeller


class Censec:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.censec_data = None
        self.Model = model

    def login(self, login, password):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='LoginTextBox']").send_keys(login)
        self.driver.find_element_by_xpath("//*[@id='SenhaTextBox']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='EntrarButton']").click()

    def search(self, cpf_cnpj):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("menucentrais")).perform()
        sleep(1)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='ctl00_CESDILi']/a")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='ctl00_CESDIConsultaAtoHyperLink']").click()
        self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_DocumentoTextBox']").send_keys(cpf_cnpj)
        self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_BuscarButton']").click()

    def get_results(self):
        self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ResultadoBuscaGeralPanel']/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_VisualizarButton']").click()
        carga = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_CodigoTextBox']").get_attribute("value")
        mes = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_MesReferenciaDropDownList']").get_attribute("value")
        ano = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_AnoReferenciaDropDownList']").get_attribute("value")
        ato = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_TipoAtoDropDownList']").get_attribute("value")
        dataAtoDia = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_DiaAtoTextBox']").get_attribute("value")
        dataAtoMes = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_MesAtoTextBox']").get_attribute("value")
        dataAtoAno = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_AnoAtoTextBox']").get_attribute("value")
        partes = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_PartesUpdatePanel']/table/tbody").text

        temp = mes, '/', ano
        data = str(temp)
        temp = dataAtoDia, '/', dataAtoMes, '/', dataAtoAno
        data_ato = str(temp)

        self.censec_data = modeller.Censec(carga, ''.join(data), ato, data_ato, partes, self.Model.search_hash)
        self.driver.quit()

        # return self.censec_data
