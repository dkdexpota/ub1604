from selenium import webdriver
import time
import math
from twocaptcha import TwoCaptcha
from pexpect import popen_spawn
import pexpect
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless
driver = webdriver.Firefox(options = opts)
API = str(input())
solver = TwoCaptcha(API)
driver.get('http://coinpot.co')
time.sleep(4)
driver.find_element_by_xpath("//button[@data-target='#RegisterModal']").click()
#ИЗМЕНИТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!
driver.find_element_by_id('RegisterEmailInput').send_keys(str(input('email')))
passw = str(input('pass'))
driver.find_element_by_id('RegisterPasswordInput').send_keys(passw)
driver.find_element_by_id('RegisterConfirmPasswordInput').send_keys(passw)
driver.find_element_by_id('AcceptTermsInput').click()
"""
def kill_captha():
    driver.find_element_by_xpath("//iframe").click()

    time.sleep(4)

    iframe_path=driver.find_element_by_xpath('//iframe[@title="recaptcha challenge"]')
    driver.switch_to.frame(iframe_path)

    z=int(1)
    while z!=0:
        l=len(driver.find_elements_by_xpath('//td'))
        while l==0 or l==16:
            driver.find_element(By.XPATH, '//*[@id="recaptcha-reload-button"]').click()
            time.sleep(2)
            l=len(driver.find_elements_by_xpath('//td'))
        obg=driver.find_element_by_xpath('//strong')
        print(obg.text)
        print(driver.find_element_by_xpath('//img[1]').get_attribute('src'))
        print(l)
        answers=input().split()
        if l == 16:
            ts = 0
        elif l == 9:
            ts = 5

        while len(answers)!=0:
            for i in range(len(answers)):
                k = int(answers[i])%int(math.sqrt(l))
                if k==0:
                    k=int(math.sqrt(l))
                path = '//*[@id="rc-imageselect-target"]/table/tbody/tr['+ str(1+((int(answers[i])-1)//int(math.sqrt(l)))) +']/td[' + str(k) + ']'
                box = driver.find_element(By.XPATH, path)
                box.click()
                time.sleep(ts)
                path=path+'/div/div[1]/img'
                print(driver.find_element_by_xpath(path).get_attribute('src'))

            answers=input().split()

        driver.find_element(By.ID, 'recaptcha-verify-button').click()
        time.sleep(1)
        print(driver.find_element_by_xpath('//img[1]').get_attribute('src'))
        z=int(input('all?'))

    driver.switch_to_default_content()
    vzual = driver.find_element(By.XPATH, '//div[15]').get_attribute('style')
    driver.switch_to.frame(iframe_path)
    driver.switch_to_default_content()

kill_captha()
"""
while True:
    try:
        key = str(driver.find_element(By.XPATH, '//*[@id="RegisterForm"]').get_attribute("data-fv-addons-recaptcha2-sitekey"))
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
    driver.find_element(By.XPATH, '//*[@data-bind="click: register"]').click()
    print('yes')
except Exception:
    print('blat')
    pass

time.sleep(10)
allelements = driver.find_elements_by_xpath("//*")
ferdigtxt = []
for i in allelements:
    if i.text in ferdigtxt:
        pass
    else:
        ferdigtxt.append(i.text)
        print(i.text)
driver.quit()