from time import sleep


class Infoseg:

    def __init__(self, browser):
        self.driver = browser.driver

    def login(self, login, password):
        self.driver.find_element_by_xpath("//*[@id='formLogin:identificacao']").send_keys(login)
        self.driver.find_element_by_xpath("//*[@id='formLogin:senha']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='formLogin:btnEntrar']").click()

    def get_search(self, cpf):
        self.driver.find_element_by_xpath("//*[@id='q']").send_keys(cpf)
        self.driver.find_element_by_xpath("//*[@id='q']").click("//*[@id='salvar']").click()

    def get_results(self):
        nome_rf = self.driver.find_element_by_xpath("//*[@id='p0-SRV_PESSOAFISICA-0']/div[2]/div[1]/div/p").text
        mae_rf = self.driver.find_element_by_xpath("//*[@id='p0-SRV_PESSOAFISICA-0']/div[2]/div[2]/div/p/a").text
        cpf_rf = self.driver.find_element_by_xpath("//*[@id=p0-SRV_PESSOAFISICA-0]/div[2]/div[3]/div/p/a]").text
        nascimento_rf = self.driver.find_element_by_xpath("//*[@id='p0-SRV_PESSOAFISICA-0']/div[2]/div[4]/div/p").text
        municipio_rf = self.driver.find_element_by_xpath("//*[@id='p0-SRV_PESSOAFISICA-0']/div[2]/div[5]/div/p").text

        nome_renach = self.driver.find_element_by_xpath("//*[@id='p0-SRV_CONDUTORES-0']/div[2]/div[1]/div/p").text
        filiacao_renach = self.driver.find_element_by_xpath("//*[@id='p0-SRV_CONDUTORES-0']/div[2]/div[2]/div/p").text
        cpf_renach = self.driver.find_element_by_xpath("//*[@id='p0-SRV_CONDUTORES-0']/div[2]/div[3]/div/p/a").text
        nascimento_renach = self.driver.find_element_by_xpath("//*[@id='p0-SRV_CONDUTORES-0']/div[2]/div[4]/div/p]").text
        categoria_renach = self.driver.find_element_by_xpath("//*[@id='p0-SRV_CONDUTORES-0']/div[2]/div[5]/div/p").text
        uf_renach = self.driver.find_element_by_xpath("//*[@id='p0-SRV_CONDUTORES-0']/div[2]/div[6]/div/p]").text

        print(nome_rf)
        print(mae_rf)
        print(cpf_rf)
        print(nascimento_rf)
        print(municipio_rf)
        print(nome_renach)
        print(filiacao_renach)
        print(cpf_renach)
        print(nascimento_renach)
        print(categoria_renach)
        print(uf_renach)

        sleep(5)
        self.driver.quit()
