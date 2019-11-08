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
    username_form = browser.find_element_by_id("id_username")
    password_form = browser.find_element_by_id("id_password")
    username_form.send_keys(username)
    password_form.send_keys(password)
    submit_button = browser.find_element_by_class_name("mdl-button")
    submit_button.click()
    return browser


#def get_projects(browser):
#    if not os.path.isdir("projects"):
#        os.mkdir("projects")
#    os.chdir("projects")
#
#    browser.get("https://intra.assistants.epita.fr/projects")
#    time.sleep(5)
#    projects = []
#    to_git = None
#
#    while True:
#        try:
#            load_button = browser.find_element_by_class_name("MuiButton-outlined")
#            load_button.click()
#        except Exception as NoMoreButton:
#            print("Can't load anymore : {}".format(NoMoreButton))
#            break
#        else:
#            time.sleep(3)
#
#    for links in browser.find_elements_by_tag_name("a"):
#        link = links.get_attribute("href")
#        if link.startswith("https://intra.assistants.epita.fr/projects/"):
#            projects.append(link)
#
#    while to_git is not True and to_git is not False:
#        answer = input("git clone the projects? [y/n]: ")
#        if answer == "y":
#            to_git = True
#        if answer == "n":
#            to_git = False
#
#    for project in projects:
#        get_project(browser, project, to_git)


browser = connection()
get_homeworks(browser)
browser.quit()
