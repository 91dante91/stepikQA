import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/huge_form.html'
driver = webdriver.Chrome(service=service)

try:
    driver.get(link)
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('Hello ')
    btn = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    btn.click()
finally:
    time.sleep(20)
    driver.quit()
