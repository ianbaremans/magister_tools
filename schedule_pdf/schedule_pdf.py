#!/usr/bin/env python3

import getpass
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

delay = 30 # seconds
userdata = {}
xpaths = {  "usrTxtBox" : '//*[@id="username"]',
            "pwdTxtBox" : '//*[@id="password"]',
            "submitUsrButton": '/html/body/magister-account/div/div/div' \
                    '[2]/div[3]/div[2]/mg-username/div/form/div/' \
                    'mg-button/button',
            "submitPwdButton": '/html/body/magister-account/div/div/div' \
                    '[2]/div[3]/div[2]/mg-password-challenge/div/form/' \
                    'div[2]/mg-button/button',
            "agendaButton": '//*[@id="menuKnopAgenda"]'
        }

def get_agenda_data():
    # Waiting for the page to load
    try:
        myElem = WebDriverWait(mydriver, delay).until(
                EC.presence_of_element_located(
                    (By.XPATH, xpaths['agendaButton'])))
        print ("Page is ready!")
        mydriver.find_element_by_xpath(xpaths['agendaButton']).click()
    except TimeoutException:
        print ("Loading took too much time!")

    # Pull the agenda data
    raw_data = requests.get(mydriver.current_url)
    print(raw_data)


def login(url, usr, pwd):
   # Logging in to Magister using the userdata
    try:
        myElem = WebDriverWait(mydriver, delay).until(
                EC.presence_of_element_located(
                    (By.XPATH, xpaths['usrTxtBox'])))
        mydriver.find_element_by_xpath(xpaths['usrTxtBox']).clear()
        mydriver.find_element_by_xpath(xpaths['usrTxtBox']).send_keys(usr)
        mydriver.find_element_by_xpath(xpaths['submitUsrButton']).click()
    except TimeoutException:
        print("Usernamepage took too long to load")

    try:
        myElem = WebDriverWait(mydriver, delay).until(
                EC.presence_of_element_located(
                    (By.XPATH, xpaths['pwdTxtBox'])))
        mydriver.find_element_by_xpath(xpaths['pwdTxtBox']).clear()
        mydriver.find_element_by_xpath(xpaths['pwdTxtBox']).send_keys(pwd)
        mydriver.find_element_by_xpath(xpaths['submitPwdButton']).click()
    except TimeoutException:
        print("Passwordpage took too long to load")

def get_user_login():
    userdata["url"] = input("Enter your Magister subdomain: ")
    userdata["usr"] = input("Enter your Magister username: ")
    userdata["pwd"] = getpass.getpass("Enter your Magister password: ")


get_user_login()

# starting the Firefox webdriver
mydriver = webdriver.Firefox()
mydriver.get("http://{}.magister.net".format(userdata["url"]))
mydriver.maximize_window()

login(userdata["url"], userdata["usr"], userdata["pwd"])
get_agenda_data()

