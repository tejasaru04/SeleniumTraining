import time

from selenium import webdriver


d=webdriver.Chrome()

d.get("https://www.facebook.com/")

print(d.title)
print(d.current_url)
print(d.page_source)

time.sleep(5)
d.quit()