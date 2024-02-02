import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.citibank.co.in/ssjsps/forgetuseridmidssi.jsp")

driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

driver.find_element(By.CSS_SELECTOR,"#citiCard1").send_keys("2334")
driver.find_element(By.CSS_SELECTOR,"#citiCard2").send_keys("2334")
driver.find_element(By.CSS_SELECTOR,"#citiCard3").send_keys("2334")
driver.find_element(By.CSS_SELECTOR,"input[name='citiCard4']").send_keys("2334")

# approach 1 - not working
# driver.find_element(By.ID,"bill-date-long").send_keys("14/04/2022")

#approach 2- automate calendar
# driver.find_element(By.ID,"bill-date-long").click()
# # select year as 2022
# select_year = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
# select_year.select_by_visible_text("2022")
# # select month as Apr
# select_month = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
# select_month.select_by_visible_text("Apr")
# # select date 14
# driver.find_element(By.LINK_TEXT,"14").click()

#approach 3- js
driver.execute_script("document.querySelector('#bill-date-long').value='19/04/2002'")
# date=datetime.date.today().strftime("%d/%m/%Y")
# driver.execute_script(f"document.querySelector('#bill-date-long').value='{date}'")

#approach 3 - option 2
ele=driver.find_element(By.XPATH,"//input[@id='bill-date-long']")
driver.execute_script("arguments[0].value='19/04/2002'",ele)

time.sleep(10)
driver.quit()

