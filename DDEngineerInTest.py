from selenium import webdriver
import time

url = 'https://protonmail.com/'

driver = webdriver.Chrome('/Users/tonyl/Desktop/DDEngineerInTest/chromedriver')
driver.get(url)