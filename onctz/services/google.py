from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep


class Google:

    def __init__(self, browser):
        self.driver = browser.driver

    def search(self, query):
        self.driver.find_element_by_name('q').send_keys(query)
        try:
            self.driver.find_element_by_name('btnK').click()
        except ElementNotInteractableException:
            sleep(2)
            self.driver.find_element_by_name('btnK').click()

    def get_results(self):
        rs = []
        try:
            _results = self.driver.find_elements_by_xpath("//div[@class='g']/div/div[@class='rc']/div[@class='r']/a[not(contains(@class,'fl'))]")
        except InvalidSelectorException:
            _results = self.driver.find_elements_by_class_name('spch s2fp-h')

        for result in _results:
            ln = []
            ln.extend([result.get_attribute('href'), result.find_element_by_tag_name('h3').text])
            rs.append(ln)

        self.driver.quit()
        return rs
