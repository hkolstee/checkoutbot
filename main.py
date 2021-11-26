from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time


# detach option to allow window to stay open after script has ended
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

# Use the url of the shoe you want to buy
# url = "https://www.nike.com/nl/launch/t/nike-sb-dunk-low-pro-emea"
url = "https://www.nike.com/nl/launch/t/lahar-low-wheat-voor-dames"
driver.get(url)

# driver.maximize_window()

# accept the cookies
acceptCookies = driver.find_element(By.XPATH, '//*[@id="cookie-settings-layout"]/div/div/div/div[3]/div[1]/button')
acceptCookies.click()

# select the size
clickSize = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[11]/button')
clickSize.click()

# need workaround for buy button, fails like this
clickBuy = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/div/button')
clickBuy.click()

