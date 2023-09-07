## google-chrome --remote-debugging-port=9014 --user-data-dir="Documents"
## D:\chrome-win64\chrome.exe  --remote-debugging-port=9014 --user-data-dir="D:/Chrome Debug"
# <div type = "error" aria-live = "assertive" class = "tiktok-tfg9wk-DivTextContainer e3v3zbj0" > <span role = "status" > Maximum number of attempts reached. Try again later. < /span > </div >
# chrome  --remote-debugging-port=9015 --user-data-dir="D:/Chrome Debug"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pyautogui
from time import sleep

def getkey(phone):
    from urllib import request, parse
    import json
    import re
    data = parse.urlencode({"to": phone, "limit": 1}).encode()
    # this will make the method "POST"
    req = request.Request(
        "http://api.bonav.xyz:8888/index.php/recordretrieval", data=data)
    resp = request.urlopen(req)
    content = resp.read()
    jsoncontent = json.loads(content)
    msg = jsoncontent[0]['msg'].strip(" ")
    msg = re.sub(' +', ' ', msg)
    if len(msg) > 0:
        print("record found.")
        print("OTP: "+msg.split(" ")[1])
        return msg.split(" ")[1]
    else:
        print("no record.")
        return ""

countrydict = {'670':"timor",'62':"indonesia"}

pyautogui.click(x=200,y=200)

# service = Service()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9015")
# driver = webdriver.Chrome(service=service, options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.tiktok.com/signup/phone-or-email/phone")
#find month
driver.find_element("xpath","//*[contains(text(), 'Month')]").click()
pyautogui.typewrite("july", interval=0.3)
pyautogui.press('enter')
# find day
driver.find_element("xpath","//*[contains(text(), 'Day')]").click()
pyautogui.typewrite("20", interval=0.3)
pyautogui.press('enter')
# find year
driver.find_element("xpath","//*[contains(text(), 'Year')]").click()
pyautogui.typewrite("1991", interval=0.3)
pyautogui.press('enter')
#find phone
phone = str(67074145354)
phone = str(67074050130)
phone = str(67074113393)
separator = 3
phone_pt1 = phone[:separator]
phone_pt2 = phone[separator:]
print(phone_pt1,phone_pt2)
# driver.find_element("xpath","//input[@placeholder()= 'Phone number']").click()
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.typewrite(countrydict[str(phone_pt1)], interval=0.3)
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.typewrite(phone_pt2, interval=0.3)
#click button send code
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(5)
try:
    driver.find_element(By.CLASS_NAME, "captcha_verify_bar")
    print("Require Captcha!!")
    sleep(30)
except:
    pyautogui.keyDown('shift')
    pyautogui.press('tab')
    pyautogui.keyUp('shift')
    sleep(5)
    
driver.find_element(By.CLASS_NAME, "code-input").click()
#click register
otp = getkey(phone)
pyautogui.typewrite(otp, interval=0.3)
#submit data
pyautogui.press('tab')
pyautogui.press('enter')

sleep(10)
pyautogui.typewrite("__balonkuada50", interval=0.3)
pyautogui.press('tab')
pyautogui.typewrite("tarou"+phone_pt2, interval=0.3)
pyautogui.press('tab')
pyautogui.press('enter')


# driver.find_element("xpath", "//*[contains(text(), 'Next')]").click()
# driver.find_element(By.XPATH, '//button[text()="Send code"]').click()
