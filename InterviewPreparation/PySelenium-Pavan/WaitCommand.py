# waits
# 1. Implicit wait-- > works based on the time
# 2. Explicit wait--> works based on the condition
import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)
assert "ProtoCommerce" in driver.title
driver.find_element_by_name("name").send_keys("Karthik")
driver.find_element_by_id("exampleInputPassword1").send_keys("Passw0rd")