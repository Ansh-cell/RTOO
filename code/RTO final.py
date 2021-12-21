import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

registration_array = []
data = pd.read_excel('/Users/DataScienceTreasures/Desktop/hello2.xlsx')
path = "/Users/DataScienceTreasures/Downloads/chromedriver"
option = webdriver.ChromeOptions()
option.add_extension('/Users/DataScienceTreasures/Downloads/extension_2_7_0_0.crx')
option.page_load_strategy = 'normal'
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
    print('before enter_value')
    enter_value = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div[2]/div/div/div['
                                                  '1]/div[2]/input'))
    )
    print("after enter_value")
    if enter_value:
        print("before enter_value_v")
        enter_value_v = driver.find_element(by=By.XPATH,
                                            value='/html/body/div[1]/div/div/div/form/div[3]/div[2]/div/div/div['
                                                  '1]/div[2]/input')
        print("after enter_value_v")
        enter_value_v.click()
        time.sleep(1)
        enter_value_v.send_keys(number)
        time.sleep(1)
        enter_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div[3]/div['
                                                              '2]/div/div/div[2]/div/button[1]')
        enter_button.click()
        # time.sleep(2)
        print('before error')
        cross = driver.find_element(by=By.XPATH, value='//*[@id="primefacesmessagedlg"]/div[1]/a/span')
        cross.click()


            # print('before registration_c')
            # registration_c = WebDriverWait(driver, 7).until(
            #     EC.presence_of_element_located((By.XPATH, '//*[@id="tb_RegnNameList:0:j_idt115"]'))
            # )
            # print("after registration_c")
            # if registration_c:
            #     print("before registration_v")
            #     registration_v = driver.find_element(by=By.XPATH, value='//*[@id="tb_RegnNameList:0:j_idt115"]').text
            #     print('after registration_c')
            #     registration_array.append(registration_v)
            #     enter_value = WebDriverWait(driver, 30).until(
            #         EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
            #                                                   '2]/div/div/div[ '
            #                                                   '1]/div[2]/input'))
            #     )
            #     if enter_value:
            #         enter_value_v = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div['
            #                                                                '3]/div[2]/div/div/div[ '
            #                                                                '1]/div[2]/input')
            #         enter_value_v.click()
            #         time.sleep(1)
            #         enter_value_v.clear()

        # else:
        #     print("before cross")
        #     time.sleep(2)
        #     cross_s = WebDriverWait(driver, 30).until(
        #         EC.presence_of_element_located((By.XPATH, '//*[@id="primefacesmessagedlg"]/div[1]/a/span'))
        #     )
        #     print("before cross_s")
        #     if cross_s:
        #         print("error")
        #         # time.sleep(3)
        #         cross = driver.find_element(by=By.XPATH, value='//*[@id="primefacesmessagedlg"]/div[1]/a/span')
        #         # time.sleep(2)
        #         cross.click()
        #         print("after cross")
        #         enter_value = WebDriverWait(driver, 30).until(
        #             EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
        #                                                       '2]/div/div/div[ '
        #                                                       '1]/div[2]/input'))
        #         )
        #         print("before enter_value")
        #         if enter_value:
        #             enter_value_v = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div['
        #                                                                    '3]/div[2]/div/div/div[ '
        #                                                                    '1]/div[2]/input')
        #             print("before click")
        #             enter_value_v.click()
        #             print("after click")
        #             # time.sleep(1)
        #             print("before clear")
        #             enter_value_v.clear()
        #             print("after clear")
        #         # date_array.append('Not issued')
        #         registration_array.append('Not assigned')
        #     else:
        #         enter_value = WebDriverWait(driver, 30).until(
        #             EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
        #                                                       '2]/div/div/div[ '
        #                                                       '1]/div[2]/input'))
        #         )
        #         print("before enter_value")
        #         if enter_value:
        #             enter_value_v = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div['
        #                                                                    '3]/div[2]/div/div/div[ '
        #                                                                    '1]/div[2]/input')
        #             print("before click")
        #             enter_value_v.click()
        #             print("after click")
        #             # time.sleep(1)
        #             print("before clear")
        #             enter_value_v.clear()
        #             print("after clear")
        #         # date_array.append('Not issued')
        #         registration_array.append('Not assigned')
        #

def convert_list_to_np_array_to_dataframe():
    file_name = '/Users/DataScienceTreasures/Desktop/hello.xlsx'
    if len(registration_array) == 0:
        print('empty array')
    else:
        data['reg_number'] = pd.DataFrame(registration_array)
        # data['date'] = pd.DataFrame(date_array)
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
            time.sleep(2)  # Not needed
            enter_input_in_chassin_no(data['VIN'][x])  # error free 99%
            #            time.sleep(
            #               3
            #          )
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
