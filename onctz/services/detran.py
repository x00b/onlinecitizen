from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import onctz.api.model.models as modeller


class Detran:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.detrancnh_data = None
        self.detrancondutor_data = None
        self.detranveiculo_data = None
        self.Model = model

    def login(self, login, password):
        self.driver.find_element_by_xpath("//*[@id='form:j_id563205015_44efc1ab']").send_keys(login)
        self.driver.find_element_by_xpath("//*[@id='form:j_id563205015_44efc191']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='form:j_id563205015_44efc15b']/span").click()

    def search_condutor(self, cpf):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='navigation_a_M_16']")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='navigation_a_F_16']").click()
        self.driver.find_element_by_xpath("//*[@id='form:cpf']").send_keys(cpf)

    def get_results_condutor(self):
        self.driver.find_element_by_xpath("//*[@id='form:j_id2049423534_c43228e_content']/table[3]/tbody/tr/td/a/span").click()
        relatorio = self.driver.current_url
        self.detrancondutor_data = modeller.DetranCondutor(relatorio, self.Model.search_hash)
        self.driver.quit()
        return self.detrancondutor_data

    def search_veiculo(self, cpf_cnpj, placa):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='navigation_a_M_18']")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='navigation_a_F_18']").click()
        self.driver.find_element_by_xpath("//*[@id='form:j_id2124610415_1b3be1bd']").send_keys(placa)
        self.driver.find_element_by_xpath("//*[@id='form:j_id2124610415_1b3be1e3']").send_keys(cpf_cnpj)

    def get_results_veiculo(self):
        self.driver.find_element_by_xpath("//*[@id='form:j_id2124610415_1b3be155_content']/table[3]/tbody/tr/td/a/span").click()
        relatorio = self.driver.current_url
        self.detranveiculo_data = modeller.DetranVeiculo(relatorio, self.Model.search_hash)
        self.driver.quit()
        return self.detranveiculo_data

    def get_search_cnh(self, cpf):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='navigation_a_M_16']")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//ul/li[2]/ul/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@id='form:cpf']").send_keys(cpf)
        self.driver.find_element_by_xpath("//*[@id='form:pnQuery_content']/table[3]/tbody/tr/td/a/span").click()

    def get_results_cnh(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        foto = self.driver.find_element_by_xpath("//*[@id='form:imgFoto']").get_attribute('src')
        renach = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/span").text
        categoria = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/span").text
        emissao = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/span").text
        nascimento = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[4]/span").text
        nome_condutor = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/span").text
        nome_mae = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[2]/td/span").text
        nome_pai = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/span").text
        registro = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr/td[1]/span").text
        tipografico = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr/td[2]/span").text
        identidade = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr/td[3]/span").text
        cpf = self.driver.find_element_by_xpath("//*[@id='form:pnCNH']/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr/td[4]/span").text

        self.detrancnh_data = modeller.DetranCnh(renach, categoria, emissao, nascimento, nome_condutor, identidade, cpf, nome_mae, nome_pai, registro, tipografico, self.Model.search_hash)
        self.driver.quit()

        return self.detrancnh_data
