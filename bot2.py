import sys
import os
import importlib
import time
import random
import spintax
import requests
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Bot:

    def __init__(self, username, password):

        self.username = username                            #Give username and password in order to log-in
        self.password = password
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"        #?

        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        self.bot = webdriver.Firefox(profile, executable_path='/home/dimitris/instacomm/geckodriver')
        self.bot.set_window_size(500, 950)
        
        with open(r'posts.txt', 'r') as f:
            self.posts = [line.strip() for line in f]

    def exit(self):
        bot = self.bot
        bot.quit()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(2)

        if check_exists_by_xpath(bot, "//button[text()='Accept']" ):
            print("No cookies")
        else:
            bot.find_element_by_xpath("//button[text()='Accept']").click()
            print("Accepted cookies")

        time.sleep(2)
        bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div/div/div/div[2]/button').click()

        print("Logging in . . .")
        time.sleep(2)
        username_field = bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
        username_field.send_keys(self.username)

        find_pass_field = (
            By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
        WebDriverWait(bot, 50).until(
            EC.presence_of_element_located(find_pass_field))
        pass_field = bot.find_element(*find_pass_field)
        WebDriverWait(bot, 50).until(
            EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(self.password)
        bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
        time.sleep(2)
    
    def comment(self, comment, post):

        bot = self.bot
        url = post
        print("commenting . . . ")
        bot.get(url)
        bot.implicitly_wait(1)

        bot.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(2)

        likebtn = bot.find_elements_by_css_selector("[aria-label='Unlike']")
        checkif_liked(bot, likebtn)

        bot.find_element_by_xpath(   
                        '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button').click()

        # if check_exists_by_xpath(bot, '/html/body/div[1]/section/main/section/div'):
            # print("skipped")
            # return bot.comment(random_comment())    

        find_comment_box = (
            By.XPATH, '/html/body/div[1]/section/main/section/div[1]/form/textarea')
        WebDriverWait(bot, 50).until(
            EC.presence_of_element_located(find_comment_box))
        comment_box = bot.find_element(*find_comment_box)
        WebDriverWait(bot, 50).until(
            EC.element_to_be_clickable(find_comment_box))
        comment_box.click()
        time.sleep(1)
        comment_box.send_keys(comment)

        find_post_button = (
            By.XPATH, '/html/body/div[1]/section/main/section/div/form/button')
        WebDriverWait(bot, 50).until(
            EC.presence_of_element_located(find_post_button))
        post_button = bot.find_element(*find_post_button)
        WebDriverWait(bot, 50).until(
            EC.element_to_be_clickable(find_post_button))
        post_button.click()

        time.sleep(5)

    # def checkif_liked(self):

        # bot = self.bot
        # likebtn = bot.find_elements_by_css_selector("[aria-label='Like']")
        # btn = likebtn

        # print(btn)
        # if(btn != []):
            # bot.find_element_by_xpath(      
            # '/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
            # time.sleep(1)

def random_comment():

    with open(r'comments.txt', 'r') as f:
        comments = [line.strip() for line in f]
    
    comment = random.choice(comments)
    # print(comments)
    return comment


def get_profile():

    username = ""
    password = ""

    if len(sys.argv) != 7:
        print("Please rerun with correct arguments.")
        sys.exit
    
    for i in range(len(sys.argv)):
        if sys.argv[i]=="-u":
            username = sys.argv[i+1]
        elif sys.argv[i] == "-p":
            password = sys.argv[i+1]
        elif sys.argv[i] == "-c":
            comments = sys.argv[i+1]

    return username, password, int(comments)

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True

    return False

def print_credentials(username, password, comments):

    print("Username is:", username)
    print("Password is:", password)
    print("Number of comments per post:", comments)

def checkif_liked(bot, btn):

    print(btn)
    if(btn == []):
        bot.find_element_by_xpath(      
        '/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
        time.sleep(1)


if __name__ == '__main__':

    username, password, comments = get_profile() 
    print_credentials(username,password,comments)

    run = Bot(username,password)
    run.login()
    time.sleep(1)

    while run.posts != []:
        print(run.posts)
        post = run.posts.pop()

        for c in range(comments):
            run.comment(random_comment(), post)
            time.sleep(2)

    time.sleep(2)
    run.exit()
    
    print("You commented successfully at all posts. Congratulations!") 