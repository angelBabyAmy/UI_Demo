#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 16:13
# @Author  : 魔女小溪
# @Title : 
# @File    : capter1.py
# @Software: PyCharm
# @license: (C) Copyright 2013-2019, luhq7
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get('http://121.37.240.170:8000/zentao/user-login.html')

driver.find_element_by_id('account').send_keys('tianxiu')
driver.find_element_by_name('password').send_keys('tianxiu123456')
driver.find_element_by_id('submit').click()
locator=(By.XPATH,"//nav[@id='navbar']/ul/li[4]/a")
WebDriverWait(driver,15).until(EC.presence_of_element_located(locator))

driver.find_element_by_xpath("//nav[@id='navbar']/ul/li[4]/a").click()
