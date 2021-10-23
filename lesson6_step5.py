import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/find_link_text'

driver = webdriver.Chrome(service=service)
try:
    driver.get(link)
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = driver.find_element(By.LINK_TEXT, link_text)
    link.click()
    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
    last_name.send_keys('Petrov')
    city = driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    city.send_keys('Smolensk')
    country = driver.find_element(By.ID, 'country')
    country.send_keys('Russia')
    btn = driver.find_element(By.CLASS_NAME, 'btn-default')
    btn.click()
finally:
    time.sleep(10)
    driver.quit()
