import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://www.efi.com/")
time.sleep(10)
action =ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Products')]")).perform()
action.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Shop Floor Data Collection')]")).click().perform()