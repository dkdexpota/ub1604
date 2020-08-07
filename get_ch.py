from selenium import webdriver
import pickle
import time
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless
driver = webdriver.Firefox(options = opts)
driver.get('http://coinpot.co')
time.sleep(1)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get('http://coinpot.co/challenges')
time.sleep(10)
for i in range(89):
	stroka = "//html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[" + str(i) + "]/div/span"
	try:
		print(driver.find_elements_by_xpath(stroka)[0].text)
	except Exception:
		pass
driver.quit()