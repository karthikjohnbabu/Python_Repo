import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
driver.get("https://www.pavantestingtools.com/p/blog-page.html")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)