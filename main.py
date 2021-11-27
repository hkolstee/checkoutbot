import time
import sys

from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run(username, password, size, shoeURL = None):

    # detach option to allow window to stay open after script has ended
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)

    # Latest chrome driver
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

    # Use given url
    driver.get(shoeURL)

    # driver.maximize_window()

    acceptCookies(driver)
    
    selectSize(driver)

    # need workaround for buy button
    addToCart(driver)

# accept the cookies
def acceptCookies(driver):
    acceptCookies = driver.find_element(By.XPATH, '//*[@id="cookie-settings-layout"]/div/div/div/div[3]/div[1]/button')
    acceptCookies.click()

# select the size, hardcoded to 42 right now
def selectSize(driver):
    clickSize = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[10]/button')
    clickSize.click()

def addToCart(driver):
    pass

# Main function, only runs from command line
if __name__ == "__main__":
    # Count arguments, replace with try except blocks in future
    if ((len(sys.argv)-1) != 4):
        print('\033[95m' + "----------------------------------------------------------")
        print('\033[91m' + "To run script, use:")
        print('\033[93m' + "python3 main.py *username* *password* *size* *URL of shoe*")
        print('\033[95m' + "----------------------------------------------------------" + '\u001b[0m')
        exit()
    
    print('\033[92m' + "\nData entered" + 
            "\nUsername: " + sys.argv[1] + 
            "\nPassword: " + sys.argv[2] + 
            "\nSize: " + sys.argv[3] + 
            "\nURL: " + sys.argv[4] + '\u001b[0m')

    run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
