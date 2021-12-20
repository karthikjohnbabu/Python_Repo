# is_displayed()
# is_enabled()
# is_selected() # can be used only for check boxes and radio buttons.
import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
username= driver.find_element_by_name('name')
print(username.is_displayed()) #returns true/false based of element status
print(username.is_enabled()) # retursn true/false based of element status
pasword= driver.find_element_by_id("exampleInputPassword1")
print(pasword.is_enabled())
print(pasword.is_displayed())
username.send_keys("Karthik")
pasword.send_keys("Karthikjohnbabu")
radio = driver.find_element_by_id("inlineRadio1")
print(radio.is_selected()) #status of radio button.





