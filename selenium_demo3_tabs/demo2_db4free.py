import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.db4free.net/")

#click on phpMyAdmin »
# //b[contains(text(),'phpMyAdmin')]
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()

#switch to second tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID,"input_username").send_keys("admin")
#enter password as admin123
driver.find_element(By.ID,"input_password").send_keys("admin123")
#click on login
driver.find_element(By.ID,"input_go").click()

actual_error= driver.find_element(By.ID,"pma_errors").text
print(actual_error)

driver.close()

#switch to 1st tab
driver.switch_to.window(driver.window_handles[0])
#print the title
print(driver.title)

time.sleep(30)
driver.quit()