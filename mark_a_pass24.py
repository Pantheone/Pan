import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=option)
option.add_argument("--no-sandbox")
option.add_argument("--headless")
option.add_argument("--disable-gpu")

driver.get('http://terabox.ru/index.php')
time.sleep(2)
pass_input = driver.find_element(By.NAME, 'pass')
pass_input.clear()
pass_input.send_keys('56553837')
driver.find_element(By.NAME, "check").click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/table/tbody/tr[11]/td/form/input[3]').click()
time.sleep(3)
while 1 < 2:
    try:
        num = 2
        for num in range(2, 50):
            if (driver.find_element(By.XPATH,
                                    f'html/body/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[{num}]/td[13]').text == '00:00:00'
                    and driver.find_element(By.XPATH,
                                            f'html/body/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[{num}]/td[14]').text != '00:00:00'):

                driver.find_element(By.XPATH,
                                    f'/html/body/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[{num}]/td[14]').click()
                time.sleep(3)
            else:
                continue
                time.sleep(3)
            num += 1
    except NoSuchElementException:  # Исключение
        pass

#     driver.close()
#     driver.quit()
