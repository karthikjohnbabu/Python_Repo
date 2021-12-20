import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.expedia.co.in/")
links= driver.find_elements_by_tag_name("a")
print(len(links))
for link in links:
    print(link.text)