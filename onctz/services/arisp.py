from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import onctz.api.model.models as modeller


class Arisp:

    def __init__(self, browser):
        self.driver = browser.driver

    def search(self, cpf_cnpj):
        self.driver.find_element_by_xpath("//*[@id='btnCallLogin']").click()
        self.driver.find_element_by_xpath("//*[@id='btnAutenticar']").click()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id='liInstituicoes']/a")).perform()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='liInstituicoes']/div/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("//*[@id='Prosseguir']").click()
        self.driver.find_element_by_xpath("//*[@id='main']/div[3]/div[2]/div[1]/div/div[2]/div/input").click()
        self.driver.find_element_by_xpath("//*[@id='chkHabilitar']").click()
        self.driver.execute_script("document.getElementById('Prosseguir').click()")
        self.driver.find_element_by_xpath("//*[@id='filterDocumento']").send_keys(cpf_cnpj)
        self.driver.find_element_by_xpath("//*[@id='btnPesquisar']").click()
        self.driver.find_element_by_xpath("//*[@id='chk339']").click()
        self.driver.find_element_by_xpath("//*[@id='chk7']").click()
        self.driver.find_element_by_xpath("//*[@id='chk10']").click()
        self.driver.execute_script("document.getElementById('btnProsseguir').click()")

    def get_results(self):
        window_before = self.driver.window_handles[0]
        self.driver.find_element_by_xpath("//*[@id='panelMatriculas']/tr[2]/td[4]/a").click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        self.driver.find_element_by_xpath("/html/body/a").click()
        sleep(2)

        self.driver.switch_to_window(window_before)
        self.driver.find_element_by_xpath("//*[@id='panelMatriculas']/tr[3]/td[4]/a").click()
        window_after2 = self.driver.window_handles[2]
        self.driver.switch_to_window(window_after2)
        self.driver.find_element_by_xpath("/html/body/a").click()
        sleep(2)

        self.driver.switch_to_window(window_before)
        self.driver.find_element_by_xpath("//*[@id='panelMatriculas']/tr[4]/td[4]/a").click()
        window_after3 = self.driver.window_handles[3]
        self.driver.switch_to_window(window_after3)
        self.driver.find_element_by_xpath("/html/body/a").click()
        self.driver.switch_to_window(window_before)

        sleep(5)
        self.driver.quit()
