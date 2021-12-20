from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.find_element_by_link_text("Checkboxes").click()
checkboxes= driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()
driver.quit()

