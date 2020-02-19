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

#ИЗМЕНИТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!
driver.find_element_by_id('SignInEmailInput').send_keys('ub1604lts@gmail.com')

driver.find_element_by_id('SignInPasswordInput').send_keys('8x5h915xxx')

def kill_captha():
    driver.find_element_by_xpath("//*[@id='captchaContainer2']/div/div/iframe").click()
    time.sleep(4)
    iframe_path=driver.find_element_by_xpath('/html/body/div[16]/div[4]/iframe')
    driver.switch_to.frame(iframe_path)

    z=int(1)
    while z != 0:
        l = len(driver.find_elements_by_xpath('//td'))
        while l == 0:
            driver.find_element(By.XPATH, '//*[@id="recaptcha-reload-button"]').click()
            time.sleep(2)
            l = len(driver.find_elements_by_xpath('//td'))
        driver.find_element_by_xpath('//strong').text
        print(driver.find_element_by_xpath('//img[1]').get_attribute('src'))
        print(l)
        answers = input().split()
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
                driver.find_element(By.XPATH, path).click()
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
print('aue')
driver.find_element(By.XPATH, '//*[@data-bind="click: signIn"]').click()
time.sleep(15)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
driver.save_screenshot('scr.png')
driver.quit()
