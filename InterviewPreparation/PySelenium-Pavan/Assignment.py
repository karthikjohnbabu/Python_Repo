
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_xpath("//*[@id='checkbox-example']/fieldset/label[2]/input").click()
chkboxname= driver.find_element_by_xpath("//*[@id='checkbox-example']/fieldset/label[2]").text
print(chkboxname)
print(type(chkboxname))
dropdown=Select(driver.find_element_by_id("dropdown-class-example"))
dropdown.select_by_visible_text(chkboxname)
driver.find_element_by_id("name").send_keys(chkboxname)
driver.find_element_by_id("alertbtn").click()
alrt=driver.switch_to.alert
print(alrt.text)
new=str(alrt)
print(type(new))
if new.find(chkboxname):
    print("Alert message success")
else:
    print(" Something wrong in execution")
