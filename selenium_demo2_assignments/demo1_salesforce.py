import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
#wait for page load to complete
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

driver.find_element(By.NAME,"UserFirstName").send_keys("jack")

select_country=Select(driver.find_element(By.NAME,"CompanyCountry"))
select_country.select_by_visible_text("United Kingdom")

driver.find_element(By.XPATH,"//input[contains(@id,'UserLastName')]").send_keys("well")

# select_country.select_by_value("GB")
# select_country.select_by_index(9)
driver.find_element(By.XPATH,"(//div[@class='checkbox-ui'])[2]").click()

driver.find_element(By.NAME,"start my free trial").click()
# //h1
actual_header=driver.find_element(By.TAG_NAME,"h1").text
print(actual_header)

actual_error=driver.find_element(By.XPATH,"//span[contains(text(),'valid phone')]").text
print(actual_error)

time.sleep(5)
driver.quit()