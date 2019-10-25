from time import sleep


class Sivec:

    def __init__(self, browser):
        self.driver = browser.driver

    def login(self, login, password):
        self.driver.find_element_by_xpath("//*[@id='nomeusuario']").send_keys(login)
        self.driver.find_element_by_xpath("//*[@id='senhausuario']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='Acessar']").click()

    def search_nome(self, nome):
        self.driver.find_element_by_xpath("//*[@id='navbar-collapse-1']/ul/li[4]/a").click()
        self.driver.find_element_by_xpath("//*[@id='1']").click()
        self.driver.find_element_by_xpath("//*[@id='navbar-collapse-1']/ul/li[4]/ul/li[2]/ul/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@id='idNomePesq']").send_keys(nome)
        self.driver.find_element_by_xpath("//*[@id='procura']").click()

    def get_results_nome(self):
        self.driver.find_element_by_xpath("//*[@id='tabelaPesquisa']/tbody/tr[1]/td[1]/a").click()
        nome = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[1]/td[2]/span").text
        sexo = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[1]/td[5]/span").text
        nascimento = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[2]/td[2]/span").text
        rg = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[2]/td[5]/span").text
        tipo_rg = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[3]/td[5]/span").text
        alcunha = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[1]/td[5]/span").text
        naturalidade = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[2]/td[5]/span").text
        estado_civil = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[2]/td[2]/span").text
        nome_mae = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[6]/td[2]/span").text
        pele = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[7]/td[2]/span").text
        profissao = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[7]/td[5]/span").text
        naturalizado = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[3]/td[2]/span").text
        endereco = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[7]/div[2]/span").text
        print(nome)
        print(sexo)
        print(nascimento)
        print(rg)
        print(tipo_rg)
        print(alcunha)
        print(naturalidade)
        print(estado_civil)
        print(nome_mae)
        print(pele)
        print(profissao)
        print(naturalidade)
        print(naturalizado)
        print(endereco)
        sleep(5)
        self.driver.quit()

    def search_sap(self, matriculaSap):
        self.driver.find_element_by_xpath("//*[@id='navbar-collapse-1']/ul/li[4]/a").click()
        self.driver.find_element_by_xpath("//*[@id='1']").click()
        self.driver.find_element_by_xpath("//*[@id='navbar-collapse-1']/ul/li[4]/ul/li[2]/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@id='idValorPesq']").send_keys(matriculaSap)
        self.driver.find_element_by_xpath("//*[@id='procurar']").click()

    def get_results_sap(self):
        self.driver.find_element_by_xpath("//*[@id='tabelaPesquisa']/tbody/tr[1]/td[1]/a").click()
        nome = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[1]/td[2]/span").text
        sexo = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[1]/td[5]/span").text
        nascimento = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[2]/td[2]/span").text
        rg = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[2]/td[5]/span").text
        tipo_rg = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[2]/table/tbody/tr[3]/td[5]/span").text
        alcunha = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[1]/td[5]/span").text
        naturalidade = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[2]/td[5]/span").text
        estado_civil = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[2]/td[2]/span").text
        nome_mae = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[6]/td[2]/span").text
        pele = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[7]/td[2]/span").text
        profissao = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[7]/td[5]/span").text
        naturalizado = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[5]/div[4]/table/tbody/tr[3]/td[2]/span").text
        endereco = self.driver.find_element_by_xpath("/html/body/form[1]/div/div[7]/div[2]/span").text
        print(nome)
        print(sexo)
        print(nascimento)
        print(rg)
        print(tipo_rg)
        print(alcunha)
        print(naturalidade)
        print(estado_civil)
        print(nome_mae)
        print(pele)
        print(profissao)
        print(naturalidade)
        print(naturalizado)
        print(endereco)
        sleep(5)
        self.driver.quit()
