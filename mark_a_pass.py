import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

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
    if driver.find_element(By.XPATH, '//*[@id="block"]/table/tbody/tr/td/table/tbody/tr[2]/td[13]') != '00:00:00':
        driver.find_element(By.XPATH, '//*[@id="block"]/table/tbody/tr/td/table/tbody/tr[2]/td[14]').click()
    time.sleep(5)
    # response = requests.get('http://terabox.ru/index.php')
    # src = response.text
    # print(src)

#
# //*[@id="block"]/table/tbody/tr/td/table/tbody/tr[2]/td[12]
# /table/tbody/tr/td/table/tbody/tr[2]/td[2]
# table > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(14)
except Exception as ex:
    print()
finally:
    driver.close()
    driver.quit()
