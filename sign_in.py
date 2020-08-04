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
opts = Options()
opts.set_headless()
assert opts.headless
driver = webdriver.Firefox(options = opts)
driver.get('http://coinpot.co')
time.sleep(4)

driver.find_element_by_xpath("//button[@data-target='#SignInModal']").click()

driver.find_element_by_id('SignInEmailInput').send_keys(str(input('email')))
driver.find_element_by_id('SignInPasswordInput').send_keys(str(input('pass')))

while True:
    try:
        key = str(driver.find_element(By.XPATH, '//*[@id="SignInForm"]').get_attribute("data-fv-addons-recaptcha2-sitekey"))
        break
    except Exception:
        time.sleep(5)
        print('blat')
pole = driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
style = pole.get_attribute("style")
style = style[:len(style)-15:]
upd = "arguments[0].setAttribute('style','"+style+"')"
driver.execute_script(upd, pole)
#req
try:
    result = solver.recaptcha(sitekey=key, url='https://freebitco.in/?op=home')
    pole.send_keys(result.get('code'))
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@data-bind="click: signIn"]').click()
    print('yes')
except Exception:
    print('blat')
    pass

time.sleep(10)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
allelements = driver.find_elements_by_xpath("//*")
ferdigtxt = []
for i in allelements:
    if i.text in ferdigtxt:
        pass
    else:
        ferdigtxt.append(i.text)
        print(i.text)
driver.quit()
