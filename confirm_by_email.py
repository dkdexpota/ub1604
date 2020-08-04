from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless
src = input('src: ')
driver = webdriver.Firefox(options = opts)
driver.get(src)
time.sleep(7)
driver.quit()