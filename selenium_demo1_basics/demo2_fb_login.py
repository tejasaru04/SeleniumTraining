import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

# ele=driver.find_element(By.ID,"email")
# ele.send_keys("jack123444455@gmail.com")
time.sleep(3)
driver.find_element(By.ID,"email").send_keys("jack123444455@gmail.com")
driver.find_element(By.ID,"pass").send_keys("welcome@123")
#Click on login
driver.find_element(By.NAME,"login").click()
time.sleep(5)

driver.quit()