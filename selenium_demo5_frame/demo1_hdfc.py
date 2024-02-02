import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://netbanking.hdfcbank.com/netbanking/")

#index
# driver.switch_to.frame(0)

#name or id as string
# driver.switch_to.frame("login_page")

#WebElement
driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))
#enter userid as jack123
driver.find_element(By.NAME,"fldLoginUserId").send_keys("jack123")
#click on continue
driver.find_element(By.LINK_TEXT,"CONTINUE").click()

# switch to main html
driver.switch_to.default_content()
