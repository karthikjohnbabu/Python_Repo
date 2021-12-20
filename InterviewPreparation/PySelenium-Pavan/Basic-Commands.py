import time
from selenium import webdriver

#driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver= webdriver.Chrome(executable_path="/Users/karthikbabu/Documents/work/chromedriver")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) # Returns the title of the page.
print(driver.current_url) # current url of the page.
driver.find_element_by_xpath("//div[@id='Tabbed']/a/button").click()
time.sleep(5)
#driver.close() # will close only the focussed browser
driver.quit() # will close all the tabs and complete browser.
