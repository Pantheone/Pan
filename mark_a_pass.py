import time
import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
try:
    driver.get('http://terabox.ru/index.php')
    time.sleep(3)
    pass_input = driver.find_element(By.NAME, 'pass')
    pass_input.clear()
    pass_input.send_keys('87788758')
    driver.find_element(By.NAME, "check").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[11]/td/form/input[3]').click()
    time.sleep(5)

except Exception as ex:
    print()
finally:
    driver.close()
    driver.quit()


