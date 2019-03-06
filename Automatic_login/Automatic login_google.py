from selenium import webdriver
from time import sleep


browser = webdriver.Chrome()
browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1551668341&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fRpsCsrfState%3db361e321-56c8-bad8-91a7-6de6ab67d50a&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
browser.find_element_by_id('i0116').send_keys('z123456618@hotmail.com')
sleep(2)
browser.find_element_by_id('idSIButton9').click()
sleep(3)
browser.find_element_by_id('i0118').send_keys('gemgt4gtii')
sleep(2)
browser.find_element_by_id('idSIButton9').click()
sleep(6000)