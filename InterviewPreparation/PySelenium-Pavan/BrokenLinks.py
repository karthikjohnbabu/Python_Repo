import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(executable_path='C:\work\chromedriver.exe')
driver.get('https://www.flipkart.com/')
links = driver.find_elements_by_tag_name("a")
print(len(links))
for i in range(0, len(links)):
    responsecode = requests.get(links[i].get_attribute('href')).status_code
    print((links[i].get_attribute('href')) + " --- " + str(responsecode))
    if (responsecode == 200):
        print("Valid Link")
    else:
        print("broken/invalid link")