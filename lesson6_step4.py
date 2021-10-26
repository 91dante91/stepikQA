from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)

link = "http://suninjuly.github.io/simple_form_find_task.html"
driver = webdriver.Chrome(service=service)

try:
    driver.get(link)
    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first_name"')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last_name"')
    last_name.send_keys('Petrov')
    city = driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"')
    city.send_keys('Smolensk')
    country = driver.find_element(By.ID, 'country')
    country.send_keys('Russia')
    btn = driver.find_element(By.ID, 'submit_button')
    btn.click()
finally:
    time.sleep(30)
    driver.quit()
