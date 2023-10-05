## google-chrome --remote-debugging-port=9014 --user-data-dir="Documents"
## D:\chrome-win64\chrome.exe  --remote-debugging-port=9014 --user-data-dir="D:/Chrome Debug"
# <div type = "error" aria-live = "assertive" class = "tiktok-tfg9wk-DivTextContainer e3v3zbj0" > <span role = "status" > Maximum number of attempts reached. Try again later. < /span > </div >
#kalau windows # chrome  --remote-debugging-port=9015 --user-data-dir="D:/Chrome Debug"
#kalau linux # google-chrome --remote-debugging-port=9014 --user-data-dir="Documents"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.bigo.tv/user/register")

wait = WebDriverWait(driver, 2)


sleep(2)

phone = str(67074145354)

separator = 3
phone_pt1 = phone[:separator]
phone_pt2 = phone[separator:]

countrydict = {'670':"timor",'62':"indonesia"}

driver.find_element("xpath",'//button[@class="head-right__login__btn"]').click()
sleep(2)
driver.find_element("xpath","//a[contains(text(), 'Sign up now')]").click()
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
sleep(2)
# driver.find_element("xpath",'//div[@class="input-container"]').click()
pyautogui.typewrite(countrydict[str(phone_pt1)], interval=0.2)
# pyautogui.typewrite(phone, interval=0.2)
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.typewrite(phone_pt2, interval=0.2)
# driver.find_element("xpath",'//input[@id="iSignupAction"]').click()