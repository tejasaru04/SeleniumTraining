"""
will start at 12:25 PM IST
Task 1 (Important)
1.	Navigate onto https://www.online.citibank.co.in/
2.	Close if any pop up comes
3.	Click on Login
4.	Click on Forgot User ID?
5.	Choose Credit Card
6.	Enter credit card number as 4545 5656 8887 9998
7.	Enter cvv number
8.	Enter date as “14/04/2022”
9.	Click on Proceed
10.	 Get the text and print it “Please accept Terms and Conditions”
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.XPATH,"//a[@class='newclose']").click()
driver.find_element(By.XPATH,"//a[@class='newclose2']").click()

driver.find_element(By.XPATH,"//span[text()='Login']").click()

#switch to second tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH,"//div[contains(text(),'Forgot User ID')]").click()

driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

# 6.	Enter credit card number as 4545 5656 8887 9998
# 7.	Enter cvv number
# 8.	Enter date as “14/04/2022”
# 9.	Click on Proceed
# 10.	 Get the text and print it “Please accept Terms and Conditions”
time.sleep(5)
driver.quit()