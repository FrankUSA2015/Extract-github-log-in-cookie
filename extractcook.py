# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import json
#获得登陆成功
driver = webdriver.Chrome()
driver.get("https://github.com/login")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login_field']").send_keys("")#用户名,输入用户名
driver.find_element_by_xpath("//*[@id='password']").send_keys("")#登陆密码，输入密码
driver.find_element_by_xpath("//*[@id='login']/form/div[3]/input[4]").click()

cookies = driver.get_cookies()
print (type(cookies))
# print ("".join(cookies))
f1 = open('cookie.json', 'w')
f1.write(json.dumps(cookies,indent=1))
f1.close
