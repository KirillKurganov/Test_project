from .base_page import BasePage
import time

class RestorePasswordPage(BasePage):
    def check_url(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        url = self.browser.current_url
        print(url)
        assert 'passport.aliexpress.' in url, 'INCORRECT URL'
