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

print(driver.window_handles)

print(driver.window_handles[0])
print(driver.window_handles[1])

# driver.switch_to.window()

time.sleep(30)
driver.quit()