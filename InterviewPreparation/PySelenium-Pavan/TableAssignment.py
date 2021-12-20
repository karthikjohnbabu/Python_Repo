import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
columnsData=driver.find_elements_by_xpath("//table[@name='courses']/tbody/tr/th")
print("No of columns in the table:",len(columnsData))
for column in columnsData:
    print(column.text)

rowData= driver.find_elements_by_xpath("//table[@name='courses']/tbody/tr")
print("No of rows in the table:", len(rowData))
SecondRowData= driver.find_elements_by_xpath("//table[@name='courses']/tbody/tr[3]/td")
for data in SecondRowData:
    print(data.text)