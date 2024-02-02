import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://nasscom.in/")


action=webdriver.ActionChains(driver)

(action
 .move_to_element(driver.find_element(By.XPATH,"//a[text()='Membership']"))
 .move_to_element(driver.find_element(By.XPATH,"//a[text()='Become a Member']")).perform())


driver.find_element(By.XPATH,"//a[text()='Membership Benefits']").click()

#Click on Click to Apply Online
#Linktext or partial link text -- use font based on UI
driver.find_element(By.PARTIAL_LINK_TEXT,"CLICK TO APPLY ONLINE").click()
# //a[text()='Click to Apply Online']


time.sleep(10)
driver.quit()

