from selenium import webdriver

# message
inputString = input("Enter Message To Send: ")

# counters
counter1 = 1
counter2 = 1
counter3 = 1
counter4 = 1
counter5 = 1

# opening wa-web
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')

# reciever1
driver.find_element_by_css_selector("span[title='" + input('reciever1:') + "']").click()
while counter1 == 1:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    counter1 = counter1 + 1

# reciever2
driver.find_element_by_css_selector("span[title='" + input('reciever2:') + "']").click()
while counter2 == 1:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    counter2 = counter2 + 1

# reciever3
driver.find_element_by_css_selector("span[title='" + input('reciever3:') + "']").click()
while counter3 == 1:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    counter3 = counter3 + 1

# reciever4
driver.find_element_by_css_selector("span[title='" + input('reciever4:') + "']").click()
while counter4 == 1:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    counter4 = counter4 + 1

# reciever5
driver.find_element_by_css_selector("span[title='" + input('reciever5:') + "']").click()
while counter5 == 1:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    counter5 = counter5 + 1
