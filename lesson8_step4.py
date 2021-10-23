from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://SunInJuly.github.io/execute_script.html'
driver = webdriver.Chrome(service=service)
try:
    driver.get(link)
    x = driver.find_element(By.ID, 'input_value').text


    def calc(number):
        return math.log(abs(12 * math.sin(int(number))))


    driver.execute_script("window.scrollBy(0, 200);")
    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))
    check_box = driver.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    radio_btn_robot_rule = driver.find_element(By.ID, 'robotsRule')
    radio_btn_robot_rule.click()
    btn_submit = driver.find_element(By.CLASS_NAME, 'btn-primary')
    btn_submit.click()
finally:
    time.sleep(10)
    driver.quit()
