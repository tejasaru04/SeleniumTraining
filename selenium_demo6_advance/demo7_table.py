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
driver.get("https://datatables.net/extensions/select/examples/initialisation/checkbox.html")

for r in range(1,7):
  elements= driver.find_elements(By.XPATH,"//table[@id='example']/tbody/tr")
  row_count=len(elements)
  #print all the names
  for i in range(1,row_count+1):
    name1=driver.find_element(By.XPATH,f"//table[@id='example']/tbody/tr[{i}]/td[2]").text
    print(name1)
  if driver.find_element(By.LINK_TEXT,"Next").is_enabled():
    driver.find_element(By.LINK_TEXT,"Next").click()




time.sleep(10)
driver.quit()

