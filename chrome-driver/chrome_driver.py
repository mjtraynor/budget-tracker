from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


def open_website(exe_path: Path=Path(__file__).parent / 'chrome-driver' / 'chromedriver.exe', url: str=None):
    driver = webdriver.Chrome(exe_path)
    driver.get(url)
    
    return driver




# Using to test functions
url = 'https://global.americanexpress.com/activity/recent'

driver = open_website(url)

site_username = Aquapanther123
site_password = Rr2qPawpk4C3

driver.find_element_by_id('eliloUserID').send_keys(site_username)
driver.find_element_by_id('eliloPassword').send_keys(site_password + Keys.ENTER)

account_switch = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//section[@data-module-name='axp-account-switcher']"))
assert element_to_be_clickable(account_switch)
account_switch.click()
gold_account = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//img[@alt='American Express Gold Card']"))
assert element_to_be_clickable(gold_account)
gold_account.click()
driver.get(url)
download_button = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//button[@element='downloadfeedicon']"))
assert element_to_be_clickable(download_button)
download_button.click()
excel_button = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//label[@for='axp-activity-download-body-selection-options-type_excel']"))
assert element_to_be_clickable(excel_button)
excel_button.click()
final_download_button = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//a[@label='Download']"))
assert element_to_be_clickable(afinal_download_button)
final_download_button.click()

#account_switch = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//section[@data-module-name='axp-account-switcher']"))
#assert element_to_be_clickable(account_switch)
#account_switch.click()

#platinum_switch = WebDriverWait(driver, timeout=5).until(lambda driver: driver.find_element_by_xpath("//p[contains(text(), 'Gold Card')]"))
#assert element_to_be_clickable(account_switch)
#account_switch.click()