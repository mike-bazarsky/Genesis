from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
from tkinter import *
import re

import time


def goToGradebook(driver, info): #Opens Gradebook tab
        driver.find_element_by_xpath("//div[@class = 'headerCategories']/span[{}]".format(info[3])).click()

def openClassTab(driver, info):
    try:
        classRegEx = re.compile(r'.*' + info[4] + '.*')
        for i in range(2, 15):
            fc = driver.find_element_by_xpath("//table[@class ='notecard'][2]//tr[2]//tbody//tr[{}]//u".format(i)).text
            result = classRegEx.search(fc)
            print(fc)
            print(type(result))
            print(result)
            if result != None:
                driver.find_element_by_xpath("//table[@class ='notecard'][2]//tr[2]//tbody//tr[{}]//span[@class = 'categorytab']".format(i)).click()
                driver.implicitly_wait(10)
                time.sleep(1)
                break
    except:
        print("ooh popachki")
        None


def driver(): #collects info and sets up driver
    info = ['parents.mcvts.net', 'natalex@optonline.net', 'Natella', 6, 'English']
    driver = openGenesis(info)
    goToGradebook(driver, info)
    openClassTab(driver, info)

def openGenesis(information): #Opens Genesis and logs in
    driver = webdriver.Chrome()
    genesis = information[0]
    if 'https://' not in genesis:
        genesis = 'https://' + genesis
    driver.get(genesis)
    driver.implicitly_wait(5)
    Username = driver.find_element_by_id("j_username")
    Password = driver.find_element_by_id('j_password')
    Username.send_keys(information[1])
    Password.send_keys(information[2])
    driver.find_element_by_class_name('saveButton').click()
    driver.implicitly_wait(5)

    return driver

driver()
