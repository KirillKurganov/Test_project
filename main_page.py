from .base_page import BasePage
from .locators_for_ali import MainPageLocators
import time
from selenium.webdriver.common.keys import Keys
import re

regular_expression_for_search_goods_test_15 = r'\d\d\d,\d\d\d' ### It`s a template for checking


class MainPage(BasePage):
    def check_url(self):
        url = self.browser.current_url
        assert 'aliexpress.' in url

    def check_english(self):
        Womens_Clothing = self.browser.find_element(*MainPageLocators.TEXT_FOR_CHECK_1).text
        print(Womens_Clothing)
        assert Womens_Clothing == 'Women’s Clothing','WRONG TEXT/LANGUAGE ENG1'
        bags = self.browser.find_element(*MainPageLocators.TEXT_FOR_CHECK_2).text
        assert bags == 'Bags', 'WRONG TEXT/LANGUAGE ENG2'
        best_match = self.browser.find_element(*MainPageLocators.TEXT_FOR_CHECK_3).text
        assert best_match == 'Best Match', 'WRONG TEXT/LANGUAGE ENG3'

    def applications_is_represented_on_page(self):
        android = self.browser.find_element(*MainPageLocators.APPLICATION_FOR_ANDROID)
        ios = self.browser.find_element(*MainPageLocators.APPLICATION_FOR_IOS)

    def go_to_android_app_page(self):
        app = self.browser.find_element(*MainPageLocators.APPLICATION_FOR_ANDROID)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", app) ### Scroll page to button element
        app.click()

    def go_to_ios_app_page(self):
        app = self.browser.find_element(*MainPageLocators.APPLICATION_FOR_IOS).click()

    def check_url_google_play(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        url = self.browser.current_url
        print(url)
        assert 'play.google.com' in url, 'INCORRECT URL'
        assert 'aliexpresshd' in url, 'INCORRECT URL'

    def check_url_app_store(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        url = self.browser.current_url
        assert 'apps.apple.com' in url, 'INCORRECT URL'
        assert 'aliexpress' in url, 'INCORRECT URL'

    def check_deutsch(self):
        kategorien = self.browser.find_element(*MainPageLocators.TEXTCATEGORIES).text
        print(kategorien)
        assert kategorien == 'Kategorien', 'WRONG TEXT/LANGUAGE DEU1'

    def check_russian(self):
        categories = self.browser.find_element(*MainPageLocators.TEXTCATEGORIES).text
        assert categories == 'Категории', 'WRONG TEXT/LANGUAGE RU1'

    def go_to_authorization_page(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON_AUTHORIZATION).click()

    def we_can_find_goods(self):
        global regular_expression_for_search_goods_test_15
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys('Ball'+ Keys.ENTER)
        time.sleep(2)
        search_result = self.browser.find_element(*MainPageLocators.SEARCH_RESULT).text
        res = re.search(regular_expression_for_search_goods_test_15, str(search_result)) ### Check that we really found many goods
        assert res != None, 'SEARCH ISN`T CORRECT'








