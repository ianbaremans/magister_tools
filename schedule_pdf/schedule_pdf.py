#!/usr/bin/env python3

import getpass
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

#os.environ["PATH"] += os.pathsep + '/geckodriver/'
userdata = {}

def login(url, usr, pwd):
    xpaths = {	"usernameTxtBox" : '//*[@id="username"]',
		"passwordTxtBox" : '//*[@id="password"]',
		"submitUsrButton": '/html/body/magister-account/div/div/div[2]/div[3]/div[2]/mg-username/div/form/div/mg-button/button',
                "submitPwdButton": '/html/body/magister-account/div/div/div[2]/div[3]/div[2]/mg-password-challenge/div/form/div[2]/mg-button/button'
	    }

    mydriver = webdriver.Firefox()
    mydriver.get("http://{}.magister.net".format(userdata["url"]))
    mydriver.maximize_window()

    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(usr)
    mydriver.find_element_by_xpath(xpaths['submitUsrButton']).click()
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(pwd)
    mydriver.find_element_by_xpath(xpaths['submitPwdButton']).click()

def get_user_login():
    userdata["url"] = input("Enter your Magister subdomain: ")
    userdata["usr"] = input("Enter your Magister username: ")
    userdata["pwd"] = getpass.getpass("Enter your Magister password: ")

get_user_login()
login(userdata["url"], userdata["usr"], userdata["pwd"])

