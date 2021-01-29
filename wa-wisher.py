from selenium import webdriver
from recipients import recipients

wish = input("Enter Message To Send: ")

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')

for recipient in recipients:
	driver.find_element_by_css_selector("span[title='" + recipient + "']").click()
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(wish)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()