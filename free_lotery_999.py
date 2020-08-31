from selenium import webdriver
import time
import pickle
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless
driver = webdriver.Firefox(options = opts)
driver.get('http://coinpot.co')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(1)
driver.get('http://coinpot.co/lottery')
time.sleep(5)
n = int(driver.find_element_by_xpath('//*[@id="PageContent_FreeLotteryTickets"]').text)
print(n)
if n >= 999:
	for i in range(9):
		driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[3]/div/a[1]").click()
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[3]/div/a[2]").click()
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[3]/div/a[3]").click()
		time.sleep(1)

print(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/h3/span').text)
driver.quit()
		
