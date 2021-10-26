from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1:
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.driver = webdriver.Chrome(service=service)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.driver.get(link)
        self.driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.driver = webdriver.Chrome(service=service)

    def teardown_method(self):
        print("quit browser for test..")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.driver.get(link)
        self.driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")