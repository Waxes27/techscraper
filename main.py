import os
from tkinter import N
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys
from sqlalchemy import true
from termcolor import colored, cprint
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument('--no-sandbox')         
# options.add_argument('--disable-dev-shm-usage')        


# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)



PATH = "driver/geckodriver"
# driver = webdriver.Chrome(PATH)

# driver.get("https://businesstech.co.za/news/trending")

def get_user_preference():
    """
    Focuses on getting specific news for the user

    Returns:
        String : Full link to news topics (unsanitary)
    """
    user_in = input("Please enter a category from \nhttps://businesstech.co.za/news/: ")
    link = f"https://businesstech.co.za/news/{user_in}"
    return user_in, link

def display_stories(user_in, articles):
    cprint(f"\n\nNews in ---> {user_in.upper()} <--- News in","green",attrs=['reverse', 'blink'])
    for i in articles:
        cprint(f"\n{articles.index(i)+1}:",'green')
        print(f"\n{i.text}\n")


def main():
    user_in,link = get_user_preference()

    driver = webdriver.Firefox(executable_path=PATH, options=options)
    driver.get(link)

    articles = driver.find_elements_by_tag_name("article")

    # display_stories(user_in, articles)



    while True:
        articles = driver.find_elements_by_tag_name("article")
        display_stories(user_in,articles)


        user_story = input("Which numbered story would you like to read...[?]: ")
        os.system("clear")
        cprint(f"\n\n...[ Start of story ]...\n\n",'green')
        try:
            time.sleep(3)
            driver.get(articles[int(user_story)-1].find_element_by_class_name('post-thumbnail').get_attribute('href'))
        except:
            print("Ran into issues. Retrying...")
            time.sleep(3)
            driver.get(articles[int(user_story)-1].find_element_by_class_name('post-thumbnail').get_attribute('href'))

        news = driver.find_element_by_class_name('entry-content').text

        news_formatted = "\n".join(news.split("."))

        print(news_formatted)
        cprint(f"\n\n...[ End of story ]...\n\n",'red')
        input("...Press Enter for list of news...")
        # try:
        #     driver.back()
        # except:
        #     print("Ran into issues. Retrying...")
        #     time.sleep(3)
        #     driver.back()





    
        


main()