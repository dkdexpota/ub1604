import subprocess
from selenium import webdriver
import time
import random
import pickle
from selenium.webdriver.firefox.options import Options
cookies = pickle.load(open("cookies.pkl", "rb"))
while True:
    try:
        t = 1
        opts = Options()
        opts.set_headless()
        assert opts.headless
        driver = webdriver.Firefox(options = opts)
        driver.get('http://coinpot.co')
        time.sleep(1)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get('http://coinpot.co/challenges')
        time.sleep(15)
        check = driver.find_element_by_xpath("//html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[53]/div/span").text.split()
        print('***LOGIN***')
        while int(check[6]) < 100000:
            driver.get('http://coinpot.co/multiplier')
            time.sleep(10)
            for i in range(1, 17000):
                m = random.randint(1,2)
                if m==1:
                    if t!=1:
                        driver.execute_script("$('#highLow0').click();")
                        driver.execute_script("$('#highLow0').click();")
                    driver.execute_script("multiplierSummaryVM.startRoll(1);")
                elif m==2:
                    if t!=2:
                        driver.execute_script("$('#highLow1').click();")
                        driver.execute_script("$('#highLow1').click();")
                    driver.execute_script("multiplierSummaryVM.startRoll(1);")
                t=int(m)
                if i%500==0:
                    print(i)
                    time.sleep(25)
            time.sleep(30)
            driver.get('http://coinpot.co/challenges')
            time.sleep(10)
            check = driver.find_element_by_xpath("//html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[53]/div/span").text.split()
            print('Progress: ', check[6])
            driver.quit()
            time.sleep(15)
            opts = Options()
            opts.set_headless()
            assert opts.headless
            driver = webdriver.Firefox(options = opts)
            driver.get('http://coinpot.co')
            time.sleep(1)
            for cookie in cookies:
                driver.add_cookie(cookie)
        cmd = "sudo shutdown -h now"
        subprocess.call(cmd, shell=True)
        break
    except Exception:
        driver.quit()
        time.sleep(60)
