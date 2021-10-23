import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
link = 'http://suninjuly.github.io/find_xpath_form'
driver = webdriver.Chrome(service=service)

try:
    driver.get(link)
    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
    first_name.send_keys('Ivan')
    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
    last_name.send_keys('Petrov')
    city = driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    city.send_keys("Smolensk")
    country = driver.find_element(By.ID, 'country')
    country.send_keys('Russia')
    # Search XPATH in button text
    # btn_submit = driver.find_element(By.XPATH, '//button[text()="Submit"]')
    # Search XPATH for full path
    btn_submit = driver.find_element(By.XPATH, '//form/div[6]/button[3]')
    btn_submit.click()
finally:
    time.sleep(20)
    driver.quit()
