from selenium import webdriver


class Browser:
    driver_path = ''

    def setup(self, brand):
        if brand == 'firefox':
            _profile = webdriver.FirefoxProfile()
            _profile.set_preference("dom.webnotifications.enabled", False)
            self.driver = webdriver.Firefox(executable_path=self.driver_path, firefox_profile=_profile)
        elif brand == 'chrome':
            _profile = webdriver.ChromeOptions()
            _profile.add_experimental_option('prefs', {"download.default_directory": "./", "download.prompt_for_download": False, "plugins.always_open_pdf_externally": True})
            _profile.add_argument("--start-maximized")
            _profile.add_argument("headless")
            self.driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=_profile)
        self.driver.implicitly_wait(2)

    def navigate(self, url=None):
        if url is not None:
            self.url = url
        self.driver.get(self.url)

    def close_all_tabs(self):
        for i in range(len(self.driver.window_handles)+1):
            print(i, '\n')
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            # self.driver.switch_to.window(self.driver.window_handles[0])
