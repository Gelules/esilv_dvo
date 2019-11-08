#!/usr/bin/env python3

from selenium import webdriver
import wget
import git
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


def get_homeworks(browser):
    if not os.path.isdir("homeworks"):
        os.mkdir("homeworks")
    os.chdir("homeworks")

    projects = []
    time.sleep(5)

    course_button = browser.find_element_by_class_name("d2l-dropdown-opener")
    course_button.click()

for links in browser.find_elements_by_tag_name("a"):
        link = links.get_attribute("href")
        if link.startswith("https://intra.assistants.epita.fr/projects/"):
            projects.append(link)

    for project in projects:
        get_project(browser, project, to_git)


browser = connection()
get_homeworks(browser)
browser.quit()
