### google-chrome --remote-debugging-port=9014 --user-data-dir="Documents"

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import pyautogui

# # import os, subprocess

# # subprocess.run(["google-chrome", "--remote-debugging-port=9014", '--user-data-dir="Documents"'],shell=True)
# # print("chuwaksz")

# # os.system('google-chrome --remote-debugging-port=9014 --user-data-dir="Documents"')

# pyautogui.click(x=200,y=200)

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.tiktok.com/signup/phone-or-email/phone")
# #find month
# driver.find_element("xpath","//*[contains(text(), 'Month')]").click()
# pyautogui.typewrite("july", interval=0.3)
# pyautogui.press('enter')
# # find day
# driver.find_element("xpath","//*[contains(text(), 'Day')]").click()
# pyautogui.typewrite("20", interval=0.3)
# pyautogui.press('enter')
# # find year
# driver.find_element("xpath","//*[contains(text(), 'Year')]").click()
# pyautogui.typewrite("1991", interval=0.3)
# pyautogui.press('enter')
# #find phone
phone = str(67074098099)
phone = str(67074145354)
# separator = 3
# phone_pt1 = phone[:separator]
# phone_pt2 = phone[separator:]
# print(phone_pt1,phone_pt2)
# # driver.find_element("xpath","//input[@placeholder()= 'Phone number']").click()
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('enter')
# pyautogui.typewrite("timor", interval=0.3)
# pyautogui.press('enter')
# pyautogui.press('tab')
# pyautogui.typewrite("74098099", interval=0.3)
# #click button send code
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('enter')
# # driver.find_element(By.XPATH, '//button[text()="Send code"]').click()


def getkey(phone):
    from urllib import request, parse
    import json
    data = parse.urlencode({"to":phone,"limit":1}).encode()
    req =  request.Request("http://api.bonav.xyz:8888/index.php/recordretrieval", data=data) # this will make the method "POST"
    resp = request.urlopen(req)
    content = resp.read()
    jsoncontent = json.loads(content)
    msg = jsoncontent[0]['msg']
    return msg.split(" ")[1]
