from selenium import webdriver
import time
import random
import pickle
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
check = driver.find_element_by_xpath("//html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[53]/div/span").text.split()
t = 1
while int(check[6]) < 100000:
    driver.get('http://coinpot.co/multiplier')
    time.sleep(10)
    low = driver.find_element_by_xpath("//label[1]")
    hight = driver.find_element_by_xpath("//label[2]")
    for i in range(0, 20000):
        m = random.randint(1,2)
        if m==1:
            if t!=1:
                low.click()
            driver.execute_script("multiplierSummaryVM.startRoll(1);")
        elif m==2:
            if t!=2:
                hight.click()
            driver.execute_script("multiplierSummaryVM.startRoll(1);")
        t=int(m)
        if i%1000==0:
            print(i)
    driver.get('http://coinpot.co/challenges')
    time.sleep(10)
    check = driver.find_element_by_xpath("//html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[53]/div/span").text.split()
    print(check)
driver.quit()
