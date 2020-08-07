from selenium import webdriver
import time
import math
import paramet
from pexpect import popen_spawn
import pexpect
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless
driver = webdriver.Firefox(options = opts)
all_conf = paramet.conf() #все параметры
driver.get('http://coinpot.co')
time.sleep(4)
driver.find_element_by_xpath("//button[@data-target='#RegisterModal']").click()
driver.find_element_by_id('RegisterEmailInput').send_keys(all_conf.get('EMAIL'))
driver.find_element_by_id('RegisterPasswordInput').send_keys(all_conf.get('PASS'))
driver.find_element_by_id('RegisterConfirmPasswordInput').send_keys(all_conf.get('PASS'))
driver.find_element_by_id('AcceptTermsInput').click()

key = str(driver.find_element(By.XPATH, '//*[@id="RegisterForm"]').get_attribute("data-fv-addons-recaptcha2-sitekey"))
pole = driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
paramet.rucap(driver, all_conf.get('API'), all_conf.get('HREF'), key, pole) #капча

time.sleep(10)
allelements = driver.find_elements_by_xpath("//*")
ferdigtxt = paramet.pg_txt(allelements) #текст страницы
driver.quit()