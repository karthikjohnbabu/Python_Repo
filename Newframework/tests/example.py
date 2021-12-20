from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("[name='name']").send_keys("karthik")
driver.find_element_by_name("email").send_keys("Babu")
driver.find_element_by_id("exampleCheck1").click()
sel= Select(driver.find_element_by_id("exampleFormControlSelect1"))
sel.select_by_visible_text("Male")
driver.find_element_by_xpath("//input[@value='Submit']").click()
alertText= driver.find_element_by_css_selector("[class*='alert-success']").text
assert ("success"in alertText)
