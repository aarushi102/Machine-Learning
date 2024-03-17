from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('D:/chromedriver')
driver.get('https://www.instagram.com/')
sleep(2)

driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

driver.find_element_by_name("username").send_keys('your_username_here')
sleep(2)

driver.find_element_by_name("password").send_keys('your_password_here')
sleep(2)

driver.find_element_by_name("password").send_keys(u'\ue007')
sleep(2)