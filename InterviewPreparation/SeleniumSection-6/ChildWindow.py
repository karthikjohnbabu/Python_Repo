from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
childWindow= driver.window_handles[1]
driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)
