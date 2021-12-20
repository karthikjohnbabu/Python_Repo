from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
webelement= driver.find_element_by_css_selector("[name='name']")
driver.find_element(withTagName("label"))