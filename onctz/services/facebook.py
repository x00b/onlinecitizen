from selenium.webdriver.common.keys import Keys
from time import sleep


class Facebook:

    def __init__(self, browser):
        self.driver = browser.driver

    def navigate(self, url=None):
        if url is not None:
            self.url = url
        self.driver.get(self.url)
        self._parent = self.driver.current_window_handle

    def login(self, email, password):
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('loginbutton').click()

    def search_person(self, query):
        self.driver.find_element_by_name('q').send_keys(query)
        sleep(3)
        self.driver.find_element_by_css_selector('button._42ft').click()
        sleep(3)
        self.driver.find_element_by_link_text('Pessoas').click()

    def get_search_results(self):
        rs = self.driver.find_elements_by_class_name('_4p2o')
        sleep(1.3)
        for profiles in rs:
            for box in profiles.find_elements_by_class_name('clearfix'):
                links = box.find_elements_by_class_name('_32mo')
                for link in links:
                    link.send_keys(Keys.CONTROL + Keys.RETURN)
                    break

    def get_profile_info(self, link=None):
        # if link is not None:
            # self.profile_url = link

        # self.navigate(self.profile_url)
        sleep(1)
        _page_menu = self.driver.find_element_by_id('fbTimelineHeadline')
        sleep(0.3)
        _about_profile = _page_menu.find_elements_by_tag_name('li')
        sleep(1.1)
        for item in _about_profile:
            if "Sobre" in item.text:
                for link in item.find_elements_by_tag_name('a'):
                    self.navigate(link.get_attribute('href'))
                    # get p info
                    # self.driver.close()
                    return

    def _parse_profile_info(self, value):
        if value is 'name':
            # get_name
            print('name')
        elif value is 'pic':
            # get picture
            print('pic')
        return

    def get_all_profiles(self):
        tabs = len(self.driver.window_handles)
        print('\t', tabs, '\n')
        for i in range(1, tabs+2):
            print(i, '\n')
            self.driver.switch_to.window(self.driver.window_handles[i])
            self.get_profile_info()
