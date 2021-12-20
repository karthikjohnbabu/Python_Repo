import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text("JavaScript Alerts").click()
driver.find_element_by_xpath("//button[contains(text(),'Click for JS Prompt')]").click()
container= driver.switch_to.alert
time.sleep(3)
container.send_keys("Hi Learn with Karthik")
time.sleep(3)
container.accept()
time.sleep(3)
print(driver.find_element_by_xpath("//p[@id='result']").text)

