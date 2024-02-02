import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
#wait for page load to complete
driver.get("https://www.facebook.com/")

#find_element() --> takes only 0.5s to check the presence of element.
# if len(driver.find_elements(By.XPATH,"//button[@title='Allow all cookies']"))>0:

driver.find_element(By.XPATH,"//button[@title='Allow all cookies']").click()

#click on Create new account
driver.find_element(By.LINK_TEXT,"Create new account").click()

#enter firstname as jack
driver.find_element(By.NAME,"firstname").send_keys("jack")

#enter lastname as ken
driver.find_element(By.NAME,"lastname").send_keys("ken")

#enter password as welcome123
driver.find_element(By.ID,"password_step_input").send_keys("88887777")

#20 Dec 2000
select_day=Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text("20")

select_month=Select(driver.find_element(By.ID,"month"))
select_month.select_by_visible_text("Dec")

#select year as 2000

#click on custom
driver.find_element(By.XPATH,"//input[@value='-1']").click()

time.sleep(5)

driver.quit()