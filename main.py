
from pathlib import Path
from time import sleep
from shutil import move
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configfile import get_config_details

""" Needed for alternative amex statement instructions.
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
"""


def main():
    """This runds the main code"""
    get_amex_statements()

def get_amex_statements() -> None:
    """Connects to Amex website and downloads the latest
    statement as an excel file
    """
    config_file_path = Path(__file__).parent / 'ignore-files'
    config_name = 'amex'
    settings = ['username', 'password']

    cd_exe_path = Path(__file__).parent / 'chrome-driver/chromedriver.exe'
    site_url = 'https://global.americanexpress.com/activity/recent'
    platinum_statement_download_url = 'https://global.americanexpress.com/api/servicing/v1/financials/documents?file_format=excel&limit=34&status=posted&additional_fields=true&itemized_transactions=true&account_key=5849CF95D74C2BC6C338965EDC8D8D3E&client_id=AmexAPI'
    gold_statement_download_url = 'https://global.americanexpress.com/api/servicing/v1/financials/documents?file_format=excel&limit=6&status=posted&additional_fields=true&itemized_transactions=true&account_key=93220B663F34D970DEDFCEDDF434A736&client_id=AmexAPI'
    downloaded_file = Path('C:/Users/MT/Downloads/activity.xlsx')
    platinum_file = Path('C:/Users/MT/Desktop/Data/Personel/Financial/Credit Card/MT Amex Platinum/Statements/Amex Platinum Transactions - Current.xlsx')
    gold_file = Path('C:/Users/MT/Desktop/Data/Personel/Financial/Credit Card/MT Amex Gold/Statements/Amex Gold Transactions - Current.xlsx')
    config_settings = get_config_details(config_file_path=config_file_path, config_name=config_name, settings=settings)

    driver = webdriver.Chrome(cd_exe_path)
    driver.get(site_url)
    driver.find_element_by_id('eliloUserID').send_keys(config_settings.get('username'))
    driver.find_element_by_id('eliloPassword').send_keys(config_settings.get('password') + Keys.ENTER)
    sleep(10)
    driver.get(platinum_statement_download_url)
    sleep(10)
    move(downloaded_file, platinum_file)
    driver.get(gold_statement_download_url)
    sleep(10)
    move(downloaded_file, gold_file)
    driver.close()

    """ This is an alternative way of getting the download. Saving it here for future reference.
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
    """

def get_chase_statement():
    """Connects to Amex website and downloads the latest
    statement as an excel file
    """
    ...

def get_firsthorizon_statement():
    """Connects to Amex website and downloads the latest
    statement as an excel file
    """
    ...

def move_statement():
    """Move the statement from downlaods folder"""
    ...

def update_budget_file():
    """Refresh the budget tracket Excel file"""
    ...


if __name__ == main():
    main()