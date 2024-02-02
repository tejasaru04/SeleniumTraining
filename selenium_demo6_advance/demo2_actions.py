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
action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Membership']")).perform()


driver.find_element(By.XPATH,"//a[text()='Members Listing']").click()


time.sleep(10)
driver.quit()
