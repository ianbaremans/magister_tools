#!/usr/bin/env python3

import getpass

def user_login():
    user_url = input("Enter your Magister URL: ")
    user_name = input("Enter your Magister username: ")
    user_pwd1 = getpass.getpass("Enter your Magister password: ")
    print("thanks")

user_login()

