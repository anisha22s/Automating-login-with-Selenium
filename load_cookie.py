#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:56:50 2023

@author: anishasamant
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time
from selenium.webdriver.chrome.options import Options



options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")



driver = webdriver.Chrome(executable_path='/Applications/chromedriver', options=options)

driver.get("https://login.mailchimp.com/")

cookies = pickle.load(open("cookies.pkl","rb"))

for cookie in cookies:
    cookie['domain'] = ".mailchimp.com"
    
    try:
      driver.add_cookie(cookie)
    except Exception as e:
        print(e)
        
driver.get("https://us11.admin.mailchimp.com")
time.sleep(5)




