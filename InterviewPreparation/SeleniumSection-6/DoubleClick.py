from selenium import webdriver
from selenium.webdriver import ActionChains
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
dc=driver.find_element_by_xpath("//button[@ondblclick='myFunction()']")
rc=driver.find_element_by_xpath("//span[contains(text(),'right')]")
action=ActionChains(driver)
action.context_click(rc).perform()
action.double_click(dc).perform()
alert=driver.switch_to.alert
assert "You double clicked me.. Thank You.." == alert.text
alert.accept()