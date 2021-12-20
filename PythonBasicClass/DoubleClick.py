from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
action= ActionChains(driver)
action.move_to_element(driver.find_element_by_css_selector(".context-menu-one")).context_click().perform()
list= driver.find_element_by_css_selector(".context-menu-icon-copy"))
action.move_to_element(driver.find_element_by_tag_name("h2")).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
#actionChains.move_to_element(img).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()