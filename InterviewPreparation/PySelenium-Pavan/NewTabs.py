import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.maximize_window()
columnDriver= driver.find_element_by_xpath("//table/tbody/tr/td[1]/ul")
links=columnDriver.find_elements_by_tag_name("a")
print(len(columnDriver.find_elements_by_tag_name("a")))
for link in links:
    link.send_keys(Keys.CONTROL+Keys.RETURN)
    time.sleep(3)
handles= driver.window_handles
print(type(handles))
print(len(handles))
size = len(handles)
for x in range(size):
  if handles[x] != driver.current_window_handle:
    driver.switch_to.window(handles[x])
    print(driver.title)




