import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/redirect_accept.html'
driver = webdriver.Chrome(service=service)
try:
    driver.get(link)
    first_window = driver.window_handles[0]
    btn = driver.find_element(By.CLASS_NAME, 'btn-primary')
    btn.click()
    second_window = driver.window_handles[1]
    driver.switch_to.window(second_window)
    x = driver.find_element(By.ID, 'input_value').text


    def calc(number):
        return math.log(abs(12 * math.sin(int(number))))


    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))
    btn_submit = driver.find_element(By.CLASS_NAME, 'btn-primary')
    btn_submit.click()
finally:
    time.sleep(10)
    driver.quit()
