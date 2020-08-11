import pytest
import time
from .main_page import MainPage
from .login_page import LoginPage
from .restore_password_page import RestorePasswordPage
from .product_page import ProductPage

@pytest.mark.main_page
class TestMainPage():
    def test_should_open_in_chrome_1(self,browser):
        link = 'https://aliexpress.com/'
        page = MainPage(browser,link)
        page.open()
        page.check_url()

    def test_should_open_in_firefox_2(self,driver):
        link = 'https://aliexpress.ru/'
        page = MainPage(driver, link)
        page.open()
        page.check_url()

    def test_site_should_be_correct_for_english_language_3(self, browser):
        link = 'https://best.aliexpress.com/'
        page = MainPage(browser, link)
        page.open()
        page.check_english()

    def test_site_should_be_correct_for_deutsch_language_4(self,browser):
        link = 'https://de.aliexpress.com/'
        page = MainPage(browser, link)
        page.open()
        page.check_deutsch()

    def test_site_should_be_correct_for_russian_language_5(self,browser):
        link = 'https://aliexpress.ru/'
        page = MainPage(browser, link)
        page.open()
        page.check_russian()

    def test_application_button_is_represented_on_page_10(self,browser):
        link = 'https://aliexpress.com/'
        page = MainPage(browser,link)
        page.open()
        page.applications_is_represented_on_page()

    @pytest.mark.application
    def test_go_to_android_application_page_11(self,browser):
        link = 'https://aliexpress.com/'
        page = MainPage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_android_app_page()
        page.check_url_google_play()

    @pytest.mark.application
    def test_go_to_ios_application_page_12(self,browser):
        link = 'https://aliexpress.com/'
        page = MainPage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_ios_app_page()
        page.check_url_app_store()

    def test_we_can_find_goods_on_search_15(self,browser):
        link = 'https://aliexpress.com/'
        page = MainPage(browser, link)
        page.open()
        page.we_can_find_goods()

@pytest.mark.product_page
class TestProductPage():

    def test_goods_has_picture_and_description_16(self,browser):
        link = 'https://www.aliexpress.com/item/33009541277.html?spm=a2g0o'
        page = ProductPage(browser,link)
        page.open()
        page.goods_has_picture_and_description()

    def test_page_of_goods_contains_button_add_to_basket_17(self,browser):
        link = 'https://www.aliexpress.com/item/33009541277.html?spm=a2g0o'
        page = ProductPage(browser, link)
        page.open()
        page.button_add_to_basket_is_represented_on_page()

@pytest.mark.autorization_page
class TestAutorizationPage():
    def test_can_switch_to_authorization_page_from_main_6(self,browser):
        link = 'https://best.aliexpress.com/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_authorization_page()
        page = LoginPage(browser, browser.current_url)
        time.sleep(1)
        page.check_url()

    def test_elements_present_on_authorization_page_7(self,browser):
        link = 'https://login.aliexpress.com/'
        page = LoginPage(browser, link)
        page.open()
        page.element_is_present_on_page()

    def test_appear_mistake_if_not_entered_password_9(self,browser):  ### NegativeTest
        link = 'https://login.aliexpress.com/'
        page = LoginPage(browser, link)
        page.open()
        page.login_without_password()

    def test_there_is_opportunity_log_in_with_google_account_13(self,browser):
        link = 'https://login.aliexpress.com/'
        page = LoginPage(browser,link)
        page.open()
        page.registration_with_google_account()
        page.check_google_page()

    def test_create_new_user_14(self,browser):
        link = 'https://login.aliexpress.com/'
        page = LoginPage(browser, link)
        page.open()
        page.create_new_user()

@pytest.mark.restore_password_page
class TestRestorePasswordPage():
    def test_can_go_to_restore_password_8(self,browser):
        link = 'https://login.aliexpress.com/'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_restore_password_page()
        time.sleep(3)
        page = RestorePasswordPage(browser, browser.current_url)
        page.check_url()

