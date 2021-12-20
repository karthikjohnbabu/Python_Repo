import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_id("username").send_keys("learnwithkarthik")
driver.find_element_by_id("password").send_keys("password")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("forgot_password_link").click()
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)
