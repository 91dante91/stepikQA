import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/get_attribute.html'
driver = webdriver.Chrome(service=service)

try:
    driver.get(link)
    treasure = driver.find_element(By.ID, 'treasure')
    x = treasure.get_attribute('valuex')

    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))
    robot_checkbox = driver.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    radio_btn_robot_rule = driver.find_element(By.ID, 'robotsRule')
    radio_btn_robot_rule.click()
    btn_submit = driver.find_element(By.CLASS_NAME, 'btn-default')
    btn_submit.click()
finally:
    time.sleep(10)
    driver.quit()
