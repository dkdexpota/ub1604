from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By
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
time.sleep(1)
print('**Conect**')
driver.get(all_conf.get('HREF'))
time.sleep(7)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/button").click()
time.sleep(1)
wall = driver.find_element_by_xpath("//*[@id='WithdrawalWalletAddressInput']")
for j in range(0, 40):
	wall.send_keys(Keys.BACKSPACE)
wall.send_keys(all_conf.get('WALLET'))
driver.find_element(By.XPATH, '//*[@data-bind="click: withdrawMaximum"]').click()
driver.find_element(By.XPATH, '//*[@id="WithdrawalPasswordInput"]').send_keys(all_conf.get('PASS'))
key = str(driver.find_element(By.XPATH, '//*[@id="WithdrawForm"]').get_attribute("data-fv-addons-recaptcha2-sitekey"))
pole = driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
paramet.rucap(driver, all_conf.get('API'), all_conf.get('HREF'), key, pole) #капча
driver.find_element(By.XPATH, '//*[@id="WithdrawButton"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[3]/button[2]').click()
time.sleep(3)

allelements = driver.find_elements_by_xpath("//*")
ferdigtxt = paramet.pg_txt(allelements) #текст страницы
driver.quit()