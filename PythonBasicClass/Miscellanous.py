from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Karthik")
print(driver.find_element_by_name("name").text)# this will not work in selenium

#print(driver.find_element_by_name("name").get_attribute("value")) # Java script dom feature.

#purely java script
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


