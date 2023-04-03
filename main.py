import time
import sys
import wait

from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

def run(username, password, size, shoeURL = None):

    # detach option to allow window to stay open after script has ended
    opts = ChromeOptions()
    # opts.headless = True
    opts.add_experimental_option("detach", True)
    opts.add_argument('--disable-blink-features=AutomationControlled')
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    # opts.add_argument("--allow-running-insecure-content") 
    # opts.add_argument("--disable-web-security") 
    # opts.add_argument("--allow-insecure-localhost")

    # Can't use latest because we need to modify chromedriver to avoid detection
    # driver = webdriver.Chrome(service = Service("/usr/bin/chromedriver"), options = opts)
    driver = webdriver.Chrome(service = Service("/usr/bin/chromedriver_linux"), options = opts)

    # Use given url
    driver.get(shoeURL)

    driver.set_window_size(1920, 1080)
    # driver.maximize_window()

    acceptCookies(driver)
    
    selectSize(driver, size)

    # need workaround for buy button
    addToCart(driver)

    # guestCheckOut = driver.find_element(By.XPATH, '//*[@id="qa-guest-checkout-mobile"]')
    # guestCheckOut.click()

# accept the cookies
def acceptCookies(driver):
    acceptCookies = driver.find_element(By.XPATH, '//*[@id="cookie-settings-layout"]/div/div/div/div[3]/div[1]/button')
    WebDriverWait(driver, 1000, 0.01).until(ec.element_to_be_clickable(acceptCookies))
    acceptCookies.click() 

# select the size
def selectSize(driver, size):
    clickSize = driver.find_element(By.XPATH, "//*[text()='EU " + size + "']")
    WebDriverWait(driver, 1000, 0.01).until(ec.element_to_be_clickable(clickSize))
    # clickSize.click()
    driver.execute_script("arguments[0].click();", clickSize)


# clicks the "Buy *price*" button, can't be done the simple way because the button is not interactable 
def addToCart(driver):
    # clickBuy = driver.find_element(By.XPATH, "//*[contains(text(),'Buy ')]")
    clickBuy = driver.find_element(By.XPATH, """//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/div/button""")

    driver.execute_script("arguments[0].scrollIntoView(true);", clickBuy)

    # Make selenium run a javascript click on the element
    # clickBuy.click()
    driver.execute_script("arguments[0].click();", clickBuy)

def waitForPageToLoad(TimeOutInSec):
    pass

def login(driver, username, password):
    pass

# Main function, only runs from command line
if __name__ == "__main__":
    # Count arguments, replace with try except blocks in future
    if ((len(sys.argv)-1) != 4):
        print('\033[95m' + "--------------------------------------------------------------")
        print('\033[91m' + "To run script, use:")
        print('\033[93m' + "python3 main.py *username* *password* *size(EU)* *URL of shoe*")
        print('\033[95m' + "--------------------------------------------------------------" + '\u001b[0m')
        exit()
    
    print('\033[92m' + "\nData entered" + 
            "\nUsername: " + sys.argv[1] + 
            "\nPassword: " + sys.argv[2] + 
            "\nSize: " + sys.argv[3] + 
            "\nURL: " + sys.argv[4] + '\u001b[0m')

    run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
