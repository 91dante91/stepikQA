import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


class TestUniqSelectors(unittest.TestCase):

    def test_passes_on_page_1(self):
        driver.get('http://suninjuly.github.io/registration1.html')
        first_name = driver.find_element(By.CSS_SELECTOR, '.first_block>:nth-child(1)>input')
        first_name.send_keys('Ivan')
        last_name = driver.find_element(By.CSS_SELECTOR, '.first_block>:nth-child(2)>input')
        last_name.send_keys('Petrov')
        email = driver.find_element(By.CSS_SELECTOR, '.first_block>:nth-child(3)>input')
        email.send_keys('ivanpetrov@gmail.com')
        btn = driver.find_element(By.TAG_NAME, 'button')
        btn.click()
        time.sleep(5)
        welcome_text_elt = driver.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(welcome_text_elt, 'Congratulations! You have successfully registered!')

    def test_crashes_on_page_2(self):
        driver.get('http://suninjuly.github.io/registration2.html')
        first_name = driver.find_element(By.CSS_SELECTOR, '.first_block>:nth-child(1)>input')
        first_name.send_keys('Ivan')
        last_name = driver.find_element(By.CSS_SELECTOR, '.first_block>:nth-child(2)>input')
        last_name.send_keys('Petrov')
        email = driver.find_element(By.CSS_SELECTOR, '.first_block>:nth-child(3)>input')
        email.send_keys('ivanpetrov@gmail.com')
        btn = driver.find_element(By.TAG_NAME, 'button')
        btn.click()
        time.sleep(5)
        welcome_text_elt = driver.find_element(By.TAG_NAME, 'h1').text
        driver.quit()
        self.assertEqual(welcome_text_elt, 'Congratulations! You have successfully registered!')

if __name__ == "__main__":
    unittest.main()