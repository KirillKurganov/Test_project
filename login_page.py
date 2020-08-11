from .base_page import BasePage
import time
from.locators_for_ali import LoginPageLoators
from selenium.common.exceptions import NoSuchElementException
import pytest

email = str(time.time()) + 'w@mail.ru'  ### Email for creating new users
password = '123456QWIUSjswyy1912'       ### password


class LoginPage(BasePage):

    def check_url(self):
        url = self.browser.current_url
        assert 'https://login.aliexpress.' in url, 'INCORRECT URL'

    def element_is_present_on_page(self):
        login_field = self.browser.find_element(*LoginPageLoators.INPUT_EMAIL)
        login_field.send_keys('123')
        login_field.clear()
        time.sleep(2)
        password_field = self.browser.find_element(*LoginPageLoators.INPUT_PASSWORD)
        password_field.send_keys('123')
        password_field.clear()
        time.sleep(2)
        button_sign_in = self.browser.find_element(*LoginPageLoators.BUTTON_SIGN_IN)
        button_forgot_password = self.browser.find_element(*LoginPageLoators.BUTTON_FORGOT_PASSWORD)

    def go_to_restore_password_page(self):
        button_forgot_password = self.browser.find_element(*LoginPageLoators.BUTTON_FORGOT_PASSWORD).click()

    def login_without_password(self):
        global email  ### Use email from global namespace

        part = self.browser.find_element(*LoginPageLoators.PART_SIGN_IN).click()
        with pytest.raises(NoSuchElementException):  ### Check that element is not on page!
            self.browser.find_element(*LoginPageLoators.ERROR_MESSAGE) #
            pytest.fail('THIS ELEMENT MUSTN`T BE HERE') #
        input_email = self.browser.find_element(*LoginPageLoators.INPUT_EMAIL).send_keys(email)
        button_sign_in = self.browser.find_element(*LoginPageLoators.BUTTON_SIGN_IN).click()
        error_message = self.browser.find_element(*LoginPageLoators.ERROR_MESSAGE).text
        time.sleep(1)
        assert 'Please enter your password' in error_message, 'MESSAGE IS NOT CORRECT'

    def registration_with_google_account(self):
        button_google = self.browser.find_element(*LoginPageLoators.BUTTON_GOOGLE).click()

    def check_google_page(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        url = self.browser.current_url
        assert 'accounts.google.com' in url, 'INCORRECT URL'

    def create_new_user(self):
        global email ### Save email from global namespace
        global password ### Save password from global namespace
        self.browser.find_element(*LoginPageLoators.BLOCK_REGISTRATION).click() ### Switch to registration block on page
        reg_email = self.browser.find_element(*LoginPageLoators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLoators.REG_PASSWORD)
        reg_password.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLoators.REG_BUTTON).click()
        time.sleep(3)
        profile_greeting = self.browser.find_element(*LoginPageLoators.PROFILE_GREETING).text
        assert 'Hi,' in profile_greeting, 'NEW USER WASN`T CREATED'






