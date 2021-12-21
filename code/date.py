'''print("before click_show_c")
                    click_show_c = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
                                                                  '3]/div/div/table/tbody/tr/td[8]/button'))
                    )
                    print('after_click_show_c')
                    if click_show_c:
                        print("new error")
                        time.sleep(5)
                        click_show = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/form/div[3]/div['
                                                                            '3]/div/div/table/tbody/tr/td[8]/button')
                        time.sleep(2)
                        click_show.click()
                        time.sleep(0)
                        print("before date element")
                        date = WebDriverWait(driver, 30).until(
                            EC.presence_of_element_located((By.ID, 'ptabid:regn_dt'))
                        )
                        print("before date")
                        if date:
                            date_v = driver.find_element(by=By.ID, value='ptabid:regn_dt').get_attribute('Value')
                            time.sleep(0)
                            print("before append")
                            date_array.append(date_v)
                            print("after append")
                            print("before back_button")
                            back_button = driver.find_element(by=By.XPATH, value='//*[@id="j_idt149"]')
                            back_button.click()
                            print("after back_button")
                            enter_value = WebDriverWait(driver, 30).until(
                                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/form/div[3]/div['
                                                                          '2]/div/div/div[ '
                                                                          '1]/div[2]/input'))
                            )
                            print("before enter_value")
                            if enter_value:
                                enter_value_v = driver.find_element(by=By.XPATH,
                                                                    value='/html/body/div[1]/div/div/div/form/div['
                                                                          '3]/div[2]/div/div/div[ '
                                                                          '1]/div[2]/input')
                                enter_value_v.click()
                                print("after enter_value")
                                time.sleep(0)
                                enter_value_v.clear()
                                print("value cleared")'''