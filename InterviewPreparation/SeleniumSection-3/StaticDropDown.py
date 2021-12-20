#select class provide the methods to handle the options in drop down
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Karthik")
driver.find_element_by_css_selector("input[name='name']").send_keys("Karthik")
driver.find_element_by_id("exampleCheck1").click()
dropdown=Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text('Male')
driver.find_element_by_css_selector("input[value='Submit']").click()
print(driver.find_element_by_css_selector("div[class*='alert-success']").text)

message=driver.find_element_by_css_selector("div[class*='alert-success']").text
assert "success" in message