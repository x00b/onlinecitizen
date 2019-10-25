from time import sleep
import onctz.api.model.models as modeller


class Infocrim:

    def __init__(self, browser, model):
        self.driver = browser.driver
        self.infocrim_data = None
        self.Model = model

    def login(self, login, password):
        self.driver.find_element_by_xpath("//*[@id='wrapper']/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[3]/input").send_keys(login)
        self.driver.find_element_by_xpath("//*[@id='wrapper']/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/input").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='wrapper']/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[4]/a/img").click()

    def search(self):
        self.driver.execute_script("document.getElementById('submit').click()")

    def get_results(self):
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td[2]/a").click()
        relatorio = self.driver.find_element_by_xpath("/html").text

        self.infocrim_data = modeller.Infocrim(relatorio, self.Model.search_hash)
        self.driver.quit()
        return self.infocrim_data
