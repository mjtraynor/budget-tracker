from pathlib import Path
from os import path
from selenium import webdriver


def open_website(url):
    
    driver = webdriver.Chrome(Path(path.dirname(__file__)) / 'chromedriver.exe')
    driver.get(url)
    
    return driver


# Using to test functions
url = r'https://global.americanexpress.com/activity/recent'

driver = open_website(url)