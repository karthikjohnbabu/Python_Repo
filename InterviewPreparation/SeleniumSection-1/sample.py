from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_CSS_selector("[name='name']").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")
driver.find_element_by_id("exampleFormControlSelect1")