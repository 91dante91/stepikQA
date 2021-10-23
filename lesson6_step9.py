from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link_1 = 'http://suninjuly.github.io/registration1.html'
link_2 = 'http://suninjuly.github.io/registration2.html'
driver = webdriver.Chrome(service=service)
driver.maximize_window()
try:
    driver.get(link_2)
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
    assert 'Congratulations! You have successfully registered!' == welcome_text_elt
finally:
    time.sleep(2)
    driver.quit()