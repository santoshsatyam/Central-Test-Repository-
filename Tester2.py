'''
Created on Dec 30, 2014

@author: sas6915

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://google.com/")
santosh = driver.find_element_by_xpath('//*[@id="gbqfq"]')
santosh.send_keys('mansfield')
santosh.send_keys(Keys.ENTER)