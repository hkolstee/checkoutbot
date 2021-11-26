from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# detach option to allow window to stay open after script has ended
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=opts)

# url = "https://www.nike.com/nl/launch/t/nike-sb-dunk-low-pro-emea"
url = "https://www.nike.com/nl/launch/t/lahar-low-wheat-voor-dames"

driver.get(url)

# driver.maximize_window()

acceptCookies = driver.find_element(By.XPATH, '//*[@id="cookie-settings-layout"]/div/div/div/div[3]/div[1]/button')
acceptCookies.click()

# clickItem = driver.find_element('//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/figure[25]/div/div/figcaption/div/div/div[2]/button')
# clickItem.click()