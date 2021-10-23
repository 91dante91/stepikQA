import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/selects1.html'
driver = webdriver.Chrome(service=service)
try:
    driver.get(link)
    num1 = driver.find_element(By.ID, 'num1').text
    num2 = driver.find_element(By.ID, 'num2').text
    result = int(num1) + int(num2)
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(f'{result}')
    btn_submit = driver.find_element(By.CLASS_NAME, 'btn-default')
    btn_submit.click()
finally:
    time.sleep(20)
    driver.quit()
