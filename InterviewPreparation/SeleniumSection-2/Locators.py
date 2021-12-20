from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Karthik")
driver.find_element_by_css_selector("input[name='name']").send_keys("Karthik")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_css_selector("input[value='Submit']").click()
print(driver.find_element_by_css_selector("div[class*='alert-success']").text)
#//*[contains(@class,'alert-success')]
#[class*='alert-success']
