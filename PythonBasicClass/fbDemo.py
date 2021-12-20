from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.rediff.com/")
driver.find_element_by_css_selector("a[title*='Sign in']").click()
driver.find_element_by_xpath("//input[@id='login1']").send_keys("hello")
driver.find_element_by_css_selector("input#password").send_keys("goodbye")
driver.find_element_by_xpath("//input[contains(@name,'procee')]").click()                                                                                      