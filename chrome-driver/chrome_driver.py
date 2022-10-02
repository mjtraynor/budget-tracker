from pathlib import Path
from os import path
from selenium import webdriver
from keyring import get_credential
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


def open_website(url):
    driver = webdriver.Chrome(Path(path.dirname(__file__)) / 'chromedriver.exe')
    driver.get(url)
    
    return driver

def get_amex_credentials(kc_username):
    kc_system = 'web_amex'
    creds = get_credential(kc_system, kc_username)
    kc_password = creds.password

    return kc_password


# Using to test functions
url = 'https://global.americanexpress.com/activity/recent'

driver = open_website(url)
site_password = get_amex_credentials()

site_username = input('Please enter your username: ')
site_password = get_amex_credentials(site_username)

driver.find_element_by_id('eliloUserID').send_keys(site_username)
driver.find_element_by_id('eliloPassword').send_keys(site_password + Keys.ENTER)

account_switch = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//section[@data-module-name='axp-account-switcher']"))
assert element_to_be_clickable(account_switch)
account_switch.click()

platinum_switch = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//p[contains(text(), 'Gold Card')]"))
assert element_to_be_clickable(account_switch)
account_switch.click()