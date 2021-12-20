from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.rediff.com/")
driver.find_element_by_css_selector("a[class*='signin']").click()
driver.find_element_by_xpath("//input[@id='login1']").send_keys("hello all")
driver.find_element_by_css_selector("input#password").send_keys("Password")
driver.find_element_by_xpath("//input[contains(@name,'proce')]").click()