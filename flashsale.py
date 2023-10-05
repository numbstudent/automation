## google-chrome --remote-debugging-port=9014 --user-data-dir="Documents"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
driver = webdriver.Chrome(options=chrome_options)

# # driver.get("https://www.tokopedia.com/samsung/samsung-galaxy-s22-5g-8-128gb-phantom-black-72dc6")
# #find month
# x = driver.find_element("xpath","//*[contains(text(), '+ Keranjang')]")
# sleep(5)
# parent = x.find_element("xpath","./..").click()

import datetime
target = datetime.datetime(2023, 9, 25, 14, 00)
while datetime.datetime.now() < target:
    sleep(0.1)
driver.get("https://www.tokopedia.com/samsung/samsung-galaxy-s22-5g-8gb-128gb-phantom-black-b1b5f")
