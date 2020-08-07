from twocaptcha import TwoCaptcha
from selenium import webdriver
import time
import pickle
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def conf():
	d = {}
	with open("conf.txt") as file:
		for line in file:
			key, value = line.split(":")
			d[key] = value.rstrip()

		if d.get('COIN') == 'DASH':
			d['HREF'] = 'https://coinpot.co/coin/dash'
		elif d.get('COIN') == 'BTC':
			d['HREF'] = 'http://coinpot.co/coin/bitcoincore'
		elif d.get('COIN') == 'BCH':
			d['HREF'] = 'http://coinpot.co/coin/bitcoincash'
		elif d.get('COIN') == 'DOGE':
			d['HREF'] = 'http://coinpot.co/coin/dogecoin'
		elif d.get('COIN') == 'LTC':
			d['HREF'] = 'http://coinpot.co/coin/litecoin'
	return d

def rucap(driver, API, HREF, KEY, pole):
	style = pole.get_attribute("style")
	style = style[:len(style)-15:]
	upd = "arguments[0].setAttribute('style','" + style + "')"
	driver.execute_script(upd, pole)
	
	solver = TwoCaptcha(API)
	while True:
		try:
			result = solver.recaptcha(sitekey = KEY, url = HREF)
			break
		except Exception:
			print("Captha_error")
	pole.send_keys(result.get('code'))
	time.sleep(1)

def pg_txt(elem):
	ferdigtxt = []
	for i in elem:
		if i.text in ferdigtxt:
			pass
		else:
			ferdigtxt.append(i.text)
			print(i.text)
	return ferdigtxt
