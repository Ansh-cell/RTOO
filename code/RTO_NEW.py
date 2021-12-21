import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

registration_array = []
data = pd.read_excel('/Users/DataScienceTreasures/Desktop/hello.xlsx')
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


def convert_list_to_np_array_to_dataframe():
    file_name = '/Users/DataScienceTreasures/Desktop/output.xlsx'
    if len(registration_array) == 0:
        print('empty array')
    else:
        data['reg_number'] = pd.DataFrame(registration_array)
        # data['date'] = pd.DataFrame(date_array)
        data.to_excel(file_name)


def exits():
    driver.quit()


def click_in_chassin_box(number):
    time.sleep(3)
    enter_value_v = driver.find_element(by=By.XPATH,
                                        value='/html/body/div[1]/div/div/div/form/div[3]/div[2]/div/div/div['
                                              '1]/div[2]/input')
    enter_value_v.click()
    enter_value_v.clear()
    enter_value_v.click()
    enter_value_v.send_keys(number)
    enter_value_v.send_keys(Keys.ENTER)


x = 0
try:
    element = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/form/nav/div[2]/ul[1]/li[2]/a")))
    report()  # error free
    registration_vehicle_detail()  # error free
    click_on_chassis_no()  # error free
    while x < len(data):
        click_in_chassin_box(data['VIN'][x])
        try:
            check_error = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="primefacesmessagedlg"]/div[1]/a')
            ))
            print('1')
            if check_error:
                print('2')
                time.sleep(10)
                driver.find_element(By.XPATH, '//*[@id="primefacesmessagedlg"]/div[1]/a').click()
                registration_array.append('Not assigned')
                print('3')
        except:
            print('4')
            try:
                registration_check = WebDriverWait(driver, 7).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="tb_RegnNameList:0:j_idt115"]')
                ))
                print('5')
                if registration_check:
                    print('6')
                    time.sleep(2)
                    registration = driver.find_element(by=By.XPATH, value='//*[@id="tb_RegnNameList:0:j_idt115"]').text
                    registration_array.append(registration)
                    print('7')
            except:
                print('8')
                time.sleep(2)
                registration_array.append('Not assigned')
        x += 1
    print('9')
    convert_list_to_np_array_to_dataframe()
    exits()
except:
    convert_list_to_np_array_to_dataframe()
    exits()
