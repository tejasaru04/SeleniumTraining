import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://smallpdf.com/pdf-to-word")


driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Mine\Balaji Dinakaran Profile.pdf")

time.sleep(10)
driver.quit()

