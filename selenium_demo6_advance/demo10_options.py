import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


options=webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("start-maximized")

options.add_experimental_option("prefs",{"download.default_directory":r"C:\Mine\Company\Tata Tech Jan 2024"})

options.add_experimental_option("mobileEmulation",{"deviceName":"Pixel 4"})
driver=webdriver.Chrome(options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.selenium.dev/downloads")

time.sleep(50)
driver.quit()
