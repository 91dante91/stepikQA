from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/math.html'
driver = webdriver.Chrome(service=service)

try:
    driver.get(link)
    x = driver.find_element(By.ID, 'input_value').text


    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))

    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio_btn_robot = driver.find_element(By.ID, 'robotsRule')
    radio_btn_robot.click()
    submit = driver.find_element(By.CLASS_NAME, 'btn-default')
    submit.click()
finally:
    time.sleep(3)
    driver.quit()
