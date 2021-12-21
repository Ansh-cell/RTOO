import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

date_array = []
registration_array = []
data = pd.read_excel('/Users/DataScienceTreasures/Downloads/Book2.xlsx')
path = "/Users/DataScienceTreasures/Downloads/chromedriver"
option = webdriver.ChromeOptions()
option.add_extension('/Users/DataScienceTreasures/Downloads/extension_2_7_0_0.crx')
driver = webdriver.Chrome(executable_path=path, options=option)
driver.get("https://vahan.parivahan.gov.in/vahan/vahan/ui/login/login.xhtml")
driver.maximize_window()


def report():
    report_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/form/nav/div[2]/ul[1]/li[2]/a")))
    if report_element:
        search_report_button = driver.find_element(by=By.XPATH, value="/html/body/form/nav/div[2]/ul[1]/li[2]/a")
        search_report_button.click()


def registration_vehicle_detail():
    vehicle_detail = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "vchDtlsId"))
    )
    if vehicle_detail:
        search_that_button = driver.find_element(by=By.ID, value="vchDtlsId")
        search_that_button.click()


def click_on_chassis_no():
    chassin_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="j_idt80"]/tbody/tr/td[3]/div/div[2]/span'))
    )
    if chassin_button:
        click_button = driver.find_element(by=By.XPATH, value='//*[@id="j_idt80"]/tbody/tr/td[3]/div/div[2]/span')
        click_button.click()


def enter_input_in_chassin_no(number):
    enter_value = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div[2]/div/div/div['
                                                  '1]/div[2]/input'))
    )
    if enter_value:
        enter_value_v = driver.find_element(by=By.XPATH,
                                            value='/html/body/div[1]/div/div/div/form/div[3]/div[2]/div/div/div['
                                                  '1]/div[2]/input')
        enter_value_v.click()
        time.sleep(2)
        enter_value_v.send_keys(number)
        time.sleep(1)
        enter_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div[3]/div['
                                                              '2]/div/div/div[2]/div/button[1]')
        enter_button.click()
        time.sleep(5)
        try:
            registration_c = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="tb_RegnNameList:0:j_idt115"]'))
            )
            if registration_c:
                registration_v = driver.find_element(by=By.XPATH, value='//*[@id="tb_RegnNameList:0:j_idt115"]').text
                registration_array.append(registration_v)
                click_show_c = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
                                                              '3]/div/div/table/tbody/tr/td[8]/button'))
                )
                if click_show_c:
                    click_show = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div[3]/div['
                                                                        '3]/div/div/table/tbody/tr/td[8]/button')
                    click_show.click()
                    time.sleep(3)
                    date = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'ptabid:regn_dt'))
                    )
                    if date:
                        date_v = driver.find_element(by=By.ID, value='ptabid:regn_dt').get_attribute('Value')
                        time.sleep(3)
                        date_array.append(date_v)
                        back_button = driver.find_element(by=By.XPATH, value='//*[@id="j_idt149"]')
                        back_button.click()
                        enter_value = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
                                                                      '2]/div/div/div[ '
                                                                      '1]/div[2]/input'))
                        )
                        if enter_value:
                            enter_value_v = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div['
                                                                                   '3]/div[2]/div/div/div[ '
                                                                                   '1]/div[2]/input')
                            enter_value_v.click()
                            time.sleep(3)
                            enter_value_v.clear()

        except:
            cross = driver.find_element(by=By.XPATH, value='//*[@id="primefacesmessagedlg"]/div[1]/a/span')
            cross.click()
            enter_value = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
                                                          '2]/div/div/div[ '
                                                          '1]/div[2]/input'))
            )
            if enter_value:
                enter_value_v = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div['
                                                                       '3]/div[2]/div/div/div[ '
                                                                       '1]/div[2]/input')
                enter_value_v.click()
                time.sleep(3)
                enter_value_v.clear()
            date_array.append('Not issued')
            registration_array.append('Not assigned')


def convert_list_to_np_array_to_dataframe():
    file_name = '/Users/DataScienceTreasures/Desktop/hello.xlsx'
    if len(date_array) == 0:
        print('empty array')
    else:
        data['reg_number'] = pd.DataFrame(registration_array)
        data['date'] = pd.DataFrame(date_array)
        data.to_excel(file_name)


def exits():
    driver.quit()


x = 0
try:
    element = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/form/nav/div[2]/ul[1]/li[2]/a")))
    report()  # error free
    registration_vehicle_detail()  # error free
    click_on_chassis_no()  # error free
    while x < len(data):
        try:
            time.sleep(3)     # Not needed
            enter_input_in_chassin_no(data['VIN'][x])  # error free 99%
            x += 1
        except:
            convert_list_to_np_array_to_dataframe()
            exits()
            print('break executed')
            break
    convert_list_to_np_array_to_dataframe()
    exits()
except:
    convert_list_to_np_array_to_dataframe()
    exits()
