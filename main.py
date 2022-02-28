from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import platform
from cfg import ATTEMPTS, DRIVERPATH
import time
from selenium.webdriver import ActionChains
import pandas as pd
from os import listdir
from os.path import isfile, join
import random

driver_path = [f for f in listdir(DRIVERPATH) if isfile(join(DRIVERPATH, f))][0]

df = pd.read_csv("toreport.csv")

a = 0

if platform.system() == "Linux":
    driver = webdriver.Chrome(service=Service(executable_path='/'.join([DRIVERPATH, driver_path])))
elif platform.system() == 'Windows':  # for windows
    driver = webdriver.Chrome(service=Service(executable_path='\\'.join([DRIVERPATH, driver_path])))

driver.get("http://web.telegram.org/k/")

action = ActionChains(driver)

while a < ATTEMPTS:
    try:
        print(f"Attempt: {a}")
        login_div = driver.find_element(by=By.CLASS_NAME, value='input-wrapper')
        login_button = login_div.find_element(by=By.TAG_NAME, value='button')
        login_button.click()
        a = 0
        break
    except:
        a += 1
        time.sleep(1)

while a < ATTEMPTS:
    try:
        phone_editable_div = driver.find_elements(by=By.CLASS_NAME, value='input-field-input')[1]
        phone_number = input("Enter your phone number, starting with a '+': ")
        phone_editable_div.clear()
        phone_editable_div.send_keys(phone_number)
        time.sleep(1)
        next_span = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Next')]")
        next_button = next_span.find_element(by=By.XPATH,
                                             value="..")  # driver.find_element(by=By.CLASS_NAME, value='btn-primary btn-color-primary rp')
        next_button.click()
        a = 0
        break
    except BaseException as err:
        #print(str(err))
        a += 1
        time.sleep(1)

code = input("Please enter code to log into your account (5 digits): ")
while len(code) != 5 or not code.isdigit():
    code = input("Invalid Entry. Please enter code to log into your account (5 digits): ")

while a < ATTEMPTS:
    try:
        print(f"Attempt: {a}")
        code_input = driver.find_elements(by=By.CLASS_NAME, value="input-field-input")
        print("code_input=", [el.text for el in code_input])
        code_input = code_input[a % 3]
        if not code_input.is_enabled():
            print("DISABLED")
            raise ValueError("DISABLED")
        code_input.clear()
        code_input.send_keys(code)
        code_input.send_keys(Keys.ENTER)
        a = 0
        break
    except BaseException as err:
        #print(str(err))
        a += 1
        time.sleep(1)

for element in df.Name:
    a = 0
    time.sleep(random.randrange(10, 50) / 10)
    print(f"\n\nAttempting to block: {element}")
    while a < 3:
        try:
            print(f"    Attempt: {a}")
            search_div = driver.find_element(by=By.CLASS_NAME, value="input-search")
            search_input = search_div.find_element(by=By.TAG_NAME, value='input')
            if not search_input.is_enabled():
                raise ValueError("DISABLED")
            search_input.clear()
            search_input.send_keys(element)
            search_input.send_keys(Keys.ENTER)
            time.sleep(1)
            search_results_div = driver.find_element(By.CLASS_NAME, "search-super-content-chats")
            first_result_li = search_results_div.find_element(By.TAG_NAME, "li")
            first_result_li.click()
            time.sleep(2)

            messages = driver.find_elements(By.CLASS_NAME, "message")
            if len(messages) == 0:
                print("  This account cannot be reported from the web version")
                break
            message = messages[-1]
            action.context_click(message).perform()

            context_menu = driver.find_element(By.ID, "bubble-contextmenu")
            all_children = context_menu.find_elements(By.XPATH, ".//*")
            children = [child for child in all_children if child.text == "Report" and child.tag_name == 'div']
            if len(children) == 0:  # message is sponsored
                message = messages[-2]
                action.context_click(message).perform()
                context_menu = driver.find_element(By.ID, "bubble-contextmenu")
                all_children = context_menu.find_elements(By.XPATH, ".//*")
                children = [child for child in all_children if child.text == "Report" and child.tag_name == 'div']

            child = children[0]
            child.click()
            time.sleep(1)

            popup_body_div = driver.find_element(By.CLASS_NAME, 'popup-body')
            other_button = popup_body_div.find_elements(By.TAG_NAME, 'button')[-1]
            other_button.click()
            time.sleep(0.5)

            input_field_div = driver.find_element(By.CLASS_NAME, 'input-field')
            input_field_input = input_field_div.find_element(By.CLASS_NAME, 'input-field-input')
            input_field_input.clear()
            time.sleep(0.5)
            input_field_input.send_keys("Публикация ложной информации. Призыв к насилию")

            # bottom_popup_buttons_div = driver.find_element(By.CLASS_NAME, 'popup-buttons popup-buttons-row')
            buttons = driver.find_elements(By.TAG_NAME, 'button')
            if buttons[-2].text == 'REPORT':
                buttons[-2].click()
            elif buttons[-1].text == 'REPORT':
                buttons[-1].click()

            a = 0
            print("  Blocked Successfully")
            break
        except BaseException as err:
            #print(str(err))
            a += 1
            time.sleep(1)

print("Success!")
