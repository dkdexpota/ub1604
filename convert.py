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
n = int(input('Convert: '))
k = str(input('Za raz: '))
driver = webdriver.Firefox(options = opts)
driver.get('http://coinpot.co')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(1)
print('**Conect**')
for i in range(n):
    driver.get('http://coinpot.co/coin/coinpottokens')
    time.sleep(7)
    print(driver.find_element_by_xpath("//div[@class='col-xs-12 col-lg-auto']/h3").text)
    driver.find_element_by_xpath("//button[@data-target='#ConvertModal']").click()
    Kolvo = driver.find_element_by_name('ConversionAmountInput')
    Kolvo.send_keys(Keys.BACKSPACE)
    Kolvo.send_keys(k)
    pas = driver.find_element_by_name('ConvertPasswordInput')
    for j in range(0,10):
        pas.send_keys(Keys.BACKSPACE)
    pas.send_keys(all_conf.get('PASS'))
    Select(driver.find_element_by_id('CurrencyDropdown')).select_by_value(all_conf.get('COIN'))
    driver.find_element_by_id('ConvertButton').click()
    driver.find_element_by_xpath("//button[@data-bind='text: confirmButton, click: confirm']").click()
    driver.find_element_by_xpath("//button[@data-bind='text: confirmButton, click: confirm']").click()
    print(i)
    time.sleep(2)
driver.quit()