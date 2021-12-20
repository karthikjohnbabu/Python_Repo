import time

from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://phptravels.org/clientarea.php")
driver.find_element_by_id("inputEmail").send_keys("username@gmail.com")
driver.find_element_by_id("inputPassword").send_keys("Password")
driver.find_element_by_name("rememberme").click()
#time.sleep(5)
#driver.find_element_by_xpath("//*[@id='recaptcha-anchor']/div[1]").click()
driver.find_element_by_id("login").click()