from selenium import webdriver
import time
import pickle
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import paramet
opts = Options()
opts.set_headless()
assert opts.headless
all_conf = paramet.conf() #все параметры
driver = webdriver.Firefox(options = opts)
driver.get('http://coinpot.co')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
urls = ['https://coinpot.co/coin/dash',
		'http://coinpot.co/coin/bitcoincore',
		'http://coinpot.co/coin/bitcoincash',
		'http://coinpot.co/coin/dogecoin',
		'http://coinpot.co/coin/litecoin']
for i in urls:
	driver.get(i)
	time.sleep(7)
	print(driver.find_element_by_xpath("//div[@class='col-xs-12 col-lg-auto']/h3").text)
	ch = input()
	if ch == 'yes':
		driver.find_element_by_xpath("//button[@data-target='#ConvertModal']").click()
		driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/form/div[2]/div[2]/a").click()
		
		pas = driver.find_element_by_name('ConvertPasswordInput')
		for j in range(0, 10):
			pas.send_keys(Keys.BACKSPACE)
		pas.send_keys(all_conf.get('PASS'))
		driver.find_element_by_id('ConvertButton').click()
		driver.find_element_by_xpath("//button[@data-bind='text: confirmButton, click: confirm']").click()
		driver.find_element_by_xpath("//button[@data-bind='text: confirmButton, click: confirm']").click()
	time.sleep(2)
driver.quit()
