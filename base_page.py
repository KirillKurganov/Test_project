import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class BasePage():
    def __init__(self,browser,url,timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
