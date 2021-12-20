import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Firefox(executable_path="C:\work\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("https://www.youtube.com/watch?v=QJqGINn4x-Y&t=1379s")

time.sleep(3)

action = ActionChains(driver)
action.click().perform()