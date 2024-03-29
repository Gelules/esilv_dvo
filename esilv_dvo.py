#!/usr/bin/env python3

from selenium import webdriver
import os
import time
import getpass


def connection():
    username = input("Mail : ")
    password = getpass.getpass("Mot de passe : ")

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 1)
    profile.set_preference("browser.download.panel.shown", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
            "application/zip,application/octet-stream,application/download")
    profile.set_preference("browser.download.useDownloadDir", True)
    browser = webdriver.Firefox(profile)

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

    checkbox = browser.find_element_by_name("z_h_cb_sa")
    checkbox.click()

    dl_button = browser.find_element_by_id("z_u")
    dl_button.click()

    dl_button = browser.find_elements_by_class_name("d2l-button")
    time.sleep(10)
    dl_button[7].click()

    os.chdir("..")


def get_homeworks(browser, url, name):
    browser.get(url)

    id = url.split("/")
    id = id[len(id) - 1]
    link = "https://devinci-online.brightspace.com/d2l/lms/dropbox/dropbox.d2l?ou=" + id
    browser.get(link)

    hws_url = []
    hws_name = []

    for links in browser.find_elements_by_tag_name("a"):
        link = links.get_attribute("href")
        if "/d2l/lms/dropbox/admin/mark/folder_submissions_users.d2l" in link:
            hws_url.append(link)
            hws_name.append(links.get_attribute("innerHTML"))

    for i in range(len(hws_url)):
        print("[{}] : {}".format(i, hws_name[i]))
    print("[q] : Quitter")

    choice = input("Choix : ")
    if ',' in choice:
        choice = choice.split(',')
    else:
        choice = list(choice)
    if 'q' in choice:
        return

    for c in choice:
        get_homework(browser, hws_url[int(c)], hws_name[int(c)])

    os.chdir("..")


def get_courses(browser):
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
    choice = choice.split(',')
    if 'q' in choice:
        return

    for c in choice:
        get_homeworks(browser, courses_url[int(c)], courses_name[int(c)])


browser = connection()
get_courses(browser)
browser.quit()
