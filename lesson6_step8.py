from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/registration1.html'
driver = webdriver.Chrome(service=service)
driver.maximize_window()
try:
    driver.get(link)
    first_name = driver.find_element(By.CLASS_NAME, 'first')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.CLASS_NAME, 'second')
    last_name.send_keys('Petrov')
    email = driver.find_element(By.CLASS_NAME, 'third')
    email.send_keys('ivanpetrov@gmail.com')
    btn = driver.find_element(By.TAG_NAME, 'button')
    btn.click()
    time.sleep(1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, 'h1').text
    assert 'Congratulations! You have successfully registered!' == welcome_text_elt
finally:
    time.sleep(10)
    driver.quit()