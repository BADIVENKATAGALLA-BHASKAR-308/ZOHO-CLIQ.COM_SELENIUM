import requests,time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


cliq_driver = webdriver.Chrome("chromedrive_64/chromedriver")
cliq_driver.maximize_window()
cliq_driver.get("https://www.zoho.com/cliq/")
google_account = cliq_driver.find_element_by_link_text('LOGIN').click()
time.sleep(5)

cliq_driver.find_element_by_xpath('//*[@id="signin_div"]/div[5]/span[1]').click()
time.sleep(5)
cliq_driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(input("Enter the username:-"))
cliq_driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(5)
cliq_driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(input("Enter the password:-"))
cliq_driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(30)
cliq_driver.find_element_by_xpath('//*[@id="GS-search-field"]').send_keys("VIVEK.S")
time.sleep(5)
cliq_driver.find_element_by_css_selector('div.msi-chat').click()
time.sleep(2)
count = 0 

no_of_times = int(input("enter how many no.of times you want:-"))
while True:
	time.sleep(10)
	count+=1
	if count > no_of_times:
		break
	else:
		text_button = cliq_driver.find_element_by_css_selector('div.textarea').send_keys(input("enter your messege:-"))
		act = ActionChains(cliq_driver)
		act.send_keys(Keys.RETURN).perform()












