#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:26:29 2023

@author: leenasamant
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time
from selenium.webdriver.chrome.options import Options

username = "oscarxu"
password = 'Xjr19980729!'

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")



driver = webdriver.Chrome(executable_path='/Applications/chromedriver', options=options)


# navigate to the Mailchimp login page
driver.get("https://login.mailchimp.com/")
time.sleep(5)

    

#driver.find_element_by_id("onetrust-accept-btn-handler").click()
driver.find_element("id", "onetrust-accept-btn-handler").click()
time.sleep(5)

#driver.find_element_by_id("username").send_keys("oscarxu")
driver.find_element("id", "username").send_keys(username)
#time.sleep(3)

#driver.find_element_by_id("password").send_keys("Xjr19980729!")
driver.find_element("id", "password").send_keys(password)
#time.sleep(3)


#driver.find_element_by_id("submit-btn").click()
driver.find_element("id", "submit-btn").click()
time.sleep(30)

cookies=driver.get_cookies()

pickle.dump(cookies, open("cookies.pkl", "wb"))
