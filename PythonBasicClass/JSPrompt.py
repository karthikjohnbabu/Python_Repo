import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.find_element_by_link_text("JavaScript Alerts").click()
driver.find_element_by_xpath("//button[@onclick='jsPrompt()']").click()
alert =driver.switch_to.alert
alert.send_keys("Karthik Babu ")
alert.accept()
print(driver.find_element_by_xpath("//p[@id='result']").text)
