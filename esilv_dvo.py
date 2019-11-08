#!/usr/bin/env python3

from selenium import webdriver
import wget
import os
import time
import getpass


def connection():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    browser = webdriver.Firefox()
    url = "https://devinci-online.brightspace.com"
    browser.get(url)
    username_form = browser.find_element_by_id("userNameInput")
    password_form = browser.find_element_by_id("passwordInput")
    username_form.send_keys(username)
    password_form.send_keys(password)
    submit_button = browser.find_element_by_id("submitButton")
    submit_button.click()
    return browser


def get_homework(browser, url, name):
    browser.get(url)
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)

    while True:
        pass


def get_homeworks(browser):
    if not os.path.isdir("homeworks"):
        os.mkdir("homeworks")
    os.chdir("homeworks")

    courses_url = []
    courses_name = []
    time.sleep(5)

    course_button = browser.find_element_by_class_name("d2l-dropdown-opener")
    course_button.click()

    for links in browser.find_elements_by_tag_name("a"):
        id = links.get_attribute("id")
        if "d2l_2_" in id:
            courses_url.append(links.get_attribute("href"))
            courses_name.append(links.get_attribute("innerHTML"))

    for i in range(len(courses_url)):
        print("[{}] : {}".format(i, courses_name[i]))
    print("[q] : Quitter")

    choice = input("Choix : ")
    if choice == "q":
        return

    get_homework(browser, courses_url[int(choice)], courses_name[int(choice)])


browser = connection()
get_homeworks(browser)
browser.quit()
