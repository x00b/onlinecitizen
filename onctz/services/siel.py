from time import sleep


class Siel:

    def __init__(self, browser):
        self.driver = browser.driver

    def login(self, login, password):
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(login)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/form/table/tbody/tr[3]/td[2]/input").click()

    def search(self, nome, numProcesso):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/form[2]/fieldset[1]/table/tbody/tr[1]/td[2]/input").send_keys(nome)
        self.driver.find_element_by_xpath("//*[@id='num_processo']").send_keys(numProcesso)
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

        print(nome)
        print(titulo)
        print(nascimento)
        print(zona)
        print(endereco)
        print(municipio)
        print(uf)
        print(data_domicilio)
        print(nome_pai)
        print(nome_mae)
        print(naturalidade)

        sleep(5)
        self.driver.quit()
