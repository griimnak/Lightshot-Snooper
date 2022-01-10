import string
import time
import random

from configparser import ConfigParser
from selenium import webdriver

config = ConfigParser()
config.read('settings.ini')

driver = webdriver.Chrome(executable_path= config.get('main', 'chromedriver_path'))

def query_url():
    # Generate 
    base = 'https://prnt.sc/'
    ending = ''.join(random.choices(string.ascii_lowercase+string.digits,k=6))
    url = base+ending

    # Save screenshot
    driver.get(url)
    driver.save_screenshot(f'screenshots/{ending}.png')


if __name__ == '__main__':
    while True:
        query_url()
        time.sleep(config.getint('main', 'refresh_delay'))
