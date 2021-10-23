import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome(service=service)
driver.get(link)
price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
btn_book = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'book')))
btn_book.click()
x = driver.find_element(By.ID, 'input_value').text


def calc(number):
    return math.log(abs(12 * math.sin(int(number))))


answer = driver.find_element(By.CLASS_NAME, 'form-control')
answer.send_keys(calc(x))
btn_submit = driver.find_element(By.ID, 'solve')
btn_submit.click()
time.sleep(10)
driver.quit()
