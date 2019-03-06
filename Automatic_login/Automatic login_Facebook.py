from selenium import webdriver
browser = webdriver.Chrome()

browser.get('http://www.facebook.com')

browser.find_element_by_id('email').send_keys('gemgt4gtii@gmail.com')
browser.find_element_by_id('pass').send_keys('aitf8196b12')
browser.find_element_by_id('loginbutton').click()