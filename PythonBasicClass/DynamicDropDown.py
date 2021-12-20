import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://phptravels.net/")
driver.find_element_by_id("s2id_autogen1").click()
driver.find_element_by_xpath("//div[@id='select2-drop']/div[1]/input").send_keys("bang")
time.sleep(3)
cities= driver.find_elements_by_css_selector("ul[class='select2-results']")
print(len(cities))
driver.find_element_by_xpath("//div[@id='select2-drop']//li[6]").click()
