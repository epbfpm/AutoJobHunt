from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from time import time
from selenium.webdriver.chrome.options import Options

site = 'https://www.linkedin.com/checkpoint/lg/sign-in-another-account'
username = 'epbfsp@gmail.com'
password = 'e4r5t6y7'

chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver))

# keep window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))
driver.get(url=site)

apply_username = driver.find_element(By.ID, 'username')
apply_username.send_keys(username)
apply_password = driver.find_element(By.ID, 'password')
apply_password.send_keys(password)
apply_password.send_keys(Keys.ENTER)



