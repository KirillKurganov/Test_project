import pytest
from selenium import webdriver

@pytest.fixture
def browser(): ### Fixture for Google Chrome
    print('   /start test...')
    browser = webdriver.Chrome()
    yield browser
    print('   /end of the test...')
    browser.quit()

@pytest.fixture
def driver():  ### Fixture for Firefox
    print('   /start test...')
    driver = webdriver.Firefox()
    yield driver
    print('   /end of the test...')
    driver.quit()

#https://aliexpress.com/