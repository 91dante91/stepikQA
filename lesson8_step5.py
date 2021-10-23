import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/file_input.html'
driver = webdriver.Chrome(service=service)
try:
    driver.get(link)
    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    last_name.send_keys('Petrov')
    email = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys('ivanpetrov@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    btn_file = driver.find_element(By.ID, 'file')
    btn_file.send_keys(file_path)
    btn_submit = driver.find_element(By.CLASS_NAME, 'btn-primary')
    btn_submit.click()
finally:
    time.sleep(10)
    driver.quit()
