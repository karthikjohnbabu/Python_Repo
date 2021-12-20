import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
validateText="Option3"
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert= driver.switch_to.alert
assert validateText in alert.text
alert.accept()