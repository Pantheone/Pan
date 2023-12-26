import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=option)
option.add_argument("--no-sandbox")
option.add_argument("--headless")
option.add_argument("--disable-gpu")

try:
    driver.get('http://terabox.ru/index.php')
    time.sleep(3)
    pass_input = driver.find_element(By.NAME, 'pass')
    pass_input.clear()
    pass_input.send_keys('56553837')
    driver.find_element(By.NAME, "check").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[11]/td/form/input[3]').click()
    time.sleep(30)

    num = 2
    a = f'/html/body/table/tbody/tr[{num}]/td[13]'
    b = f'/html/body/table/tbody/tr[{num}]/td[14]'

    for num in range(2, 21):
        if f'/html/body/table/tbody/tr[{num}]/td[13]' != '00:00:00' and f'/html/body/table/tbody/tr[{num}]/td[14]' == '00:00:00':
            driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[{num}]/td[14]').click()
        else:
            continue
        num += 1

    # while num < 20:
    #     if f'/html/body/table/tbody/tr[{num}]/td[13]' != '00:00:00':
    #         driver.find_element(By.XPATH, f'/html/body/table/tbody/tr[{num}]/td[14]').click()
    #     else:
    #         continue
    #     num += 1
    # if driver.find_element(By.XPATH, '//*[@id="block"]/table/tbody/tr/td/table/tbody/tr[2]/td[13]') != '00:00:00':
    #     driver.find_element(By.XPATH, '//*[@id="block"]/table/tbody/tr/td/table/tbody/tr[2]/td[14]').click()
    # time.sleep(5)
    # response = requests.get('http://terabox.ru/index.php')
    # src = response.text
    # print(src)

#
# //*[@id="block"]/table/tbody/tr/td/table/tbody/tr[2]/td[12]
# /table/tbody/tr/td/table/tbody/tr[2]/td[2]
# table > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(14)
# except Exception as ex:
#     print()
finally:
    driver.close()
    driver.quit()
