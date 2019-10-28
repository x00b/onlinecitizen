from time import sleep
import onctz.api.model.models as modeller


class Siel:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.Model = model
        self.sieldata = None

    def login(self, login, password):
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(login)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/form/table/tbody/tr[3]/td[2]/input").click()

    def search(self, nome, numprocesso="123"):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/form[2]/fieldset[1]/table/tbody/tr[1]/td[2]/input").send_keys(nome)
        self.driver.find_element_by_xpath("//*[@id='num_processo']").send_keys(numprocesso)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/form[2]/table/tbody/tr/td[2]/input").click()

    def get_results(self):
        nome = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[2]/td[2]").text
        titulo = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[3]/td[2]").text
        nascimento = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[4]/td[2]").text
        zona = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[5]/td[2]").text
        endereco = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[6]/td[2]").text
        municipio = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[7]/td[2]").text
        uf = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[8]/td[2]").text
        data_domicilio = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[9]/td[2]").text
        nome_pai = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[10]/td[2]").text
        nome_mae = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[11]/td[2]").text
        naturalidade = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/table/tbody/tr[12]/td[2]").text

        self.sieldata = modeller.Siel(nome, titulo, nascimento, zona, endereco, municipio, uf, data_domicilio, nome_pai, nome_mae, naturalidade, self.Model.search_hash)
        self.driver.quit()
        return self.sieldata
