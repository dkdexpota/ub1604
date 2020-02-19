from selenium import webdriver
import pickle
import time
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
print(driver.find_elements_by_xpath("//html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[53]/div/span")[0].text)
print(driver.find_elements_by_xpath("//html/body/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[88]/div/span")[0].text)
driver.quit()
