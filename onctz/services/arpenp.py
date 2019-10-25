from time import sleep
import onctz.api.model.models as modeller


class Arpenp:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.Model = model

    def search(self, numProcesso):
        self.driver.find_element_by_xpath("//div/a[@href='pagina2-pesquisa.html']/img").click()
        sleep(1)
        self.driver.find_element_by_xpath("//li[@class='item3']/a").click()
        self.driver.find_element_by_xpath("//a[@href='pagina3-busca.html']").click()
        self.driver.find_element_by_xpath("//tbody/tr/td/input[@value='N,TN']").click()
        self.driver.find_element_by_name('numero_processo').send_keys(numProcesso)
        self.driver.find_element_by_name('vara_juiz_id').click()
        self.driver.find_element_by_xpath("//td/select/option[@value='297']").click()
        self.driver.find_element_by_name('btn_pesquisar').click()

    def get_results(self):
        cartorioRegistro = self.driver.find_element_by_xpath("//table/tbody/tr[1]/td/b").text
        numeroCns = self.driver.find_element_by_xpath("//table/tbody/tr[2]/td/b").text
        uf = self.driver.find_element_by_xpath("//table/tbody/tr[3]/td/b").text
        nomeConjuge1 = self.driver.find_element_by_xpath("//table[2]/tbody/tr[2]/td[2]").text
        novoNomeConjuge1 = self.driver.find_element_by_xpath("//table[2]/tbody/tr[3]/td[2]").text
        nomeConjuge2 = self.driver.find_element_by_xpath("//table[2]/tbody/tr[4]/td[2]").text
        novoNomeConjuge2 = self.driver.find_element_by_xpath("//table[2]/tbody/tr[5]/td[2]").text
        dataCasamento = self.driver.find_element_by_xpath("//table[2]/tbody/tr[6]/td[2]").text
        matricula = self.driver.find_element_by_xpath("//table[2]/tbody/tr[8]/td[2]").text
        dataEntrada = self.driver.find_element_by_xpath("//table[2]/tbody/tr[9]/td[2]").text
        dataRegistro = self.driver.find_element_by_xpath("//table[2]/tbody/tr[10]/td[2]").text

        self.arpenp_data = modeller.Arpenp(cartorioRegistro, numeroCns, uf, nomeConjuge1, novoNomeConjuge1, nomeConjuge2, novoNomeConjuge2, dataCasamento, matricula, dataEntrada, dataRegistro, self.Model.search_hash)
        self.driver.quit()
        return self.arpenp_data
