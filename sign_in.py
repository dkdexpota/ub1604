from selenium import webdriver
import time
import pickle
import math
import random
import subprocess
from pexpect import popen_spawn
import pexpect
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import paramet
all_conf = paramet.conf() #все параметры
opts = Options()
opts.set_headless()
assert opts.headless
driver = webdriver.Firefox(options = opts)
driver.get('http://coinpot.co')
time.sleep(4)
driver.find_element_by_xpath("//button[@data-target='#SignInModal']").click()

driver.find_element_by_id('SignInEmailInput').send_keys(all_conf.get('EMAIL'))
driver.find_element_by_id('SignInPasswordInput').send_keys(all_conf.get('PASS'))

key = str(driver.find_element(By.XPATH, '//*[@id="SignInForm"]').get_attribute("data-fv-addons-recaptcha2-sitekey"))
pole = driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response-1"]')

paramet.rucap(driver, all_conf.get('API'), all_conf.get('HREF'), key, pole) #капча

time.sleep(10)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
allelements = driver.find_elements_by_xpath("//*")
ferdigtxt = paramet.pg_txt(allelements) #текст страницы
driver.quit()
