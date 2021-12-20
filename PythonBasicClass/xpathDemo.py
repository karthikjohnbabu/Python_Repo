from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//input[@name='email']").send_keys("my own xpath")
driver.find_element_by_xpath("//*[@id='pass']").send_keys("password")
driver.find_element_by_xpath("//input[@type='submit']").click()
