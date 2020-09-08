from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.config import settings
from utilities.text_reader_n_writer import read_write_txt


class Application:
    """ This class and its functions are for application handling"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Application()
        return cls.instance

    def __init__(self):
        # # FOR EXECUTION ON WINDOWS >>>>>>>>>>>>>
        # chrome_path = os.path.join(projectPath, 'resources/chromedriver_81.exe')
        # chrome_options = Options()
        # chrome_options.headless = False
        # chrome_options.add_argument('--lang=en-us')
        # chrome_options.add_argument("--disable-extensions")
        # self.driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
        # self.driver.maximize_window()

        # FOR EXECUTION ON LINUX >>>>>>>>>>>>>
        # chrome_options = Options()
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--no-sandbox")
        # prefs = {
        #     "translate_whitelists": {"your native language": "en"},
        #     "translate": {"enabled": "True"}
        # }
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.headless = True
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument("--window-size=1366x768x24")
        #
        # # 2020-09-02 ESilva Solving issue part_1: Access denied / You don't have access permission to access...
        # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        # chrome_options.add_argument('user-agent={0}'.format(user_agent))
        #
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver.fullscreen_window()
        # self.driver.maximize_window()
        # size = self.driver.get_window_size()
        # print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))
        #
        # # 2020-09-02 ESilva Solving issue part_2: Access denied / You don't have access permission to access...
        # self.driver.get("https://www.trivago.es") # not clear why but first time we hit the site we get an access denied :/
        # self.driver.implicitly_wait(1)

        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.headless = True
        # chrome_options.binary_location = "snap/bin/chromium"
        # chrome_options.binary_location = "resources/chromedriver"
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=960x720x24")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.fullscreen_window()

    def get_driver(self):
        return self.driver

    def close_driver(self):
        return self.driver.close()

    def load_website(self):
        app_url = settings['application_url']
        print("APP URL::", app_url)
        app.open_url(app_url)

    def goto_page(self, page):
        environment_variables = read_write_txt.reading_environment_variables()
        self.driver.get(urljoin(environment_variables['URL'], page))

    def open_url(self, str_url):
        self.driver.get(str_url)
        self.driver.implicitly_wait(5)
        print(len(self.driver.page_source))

    def close_entire_browser(self):
        self.driver.quit()


app = Application.get_instance()

