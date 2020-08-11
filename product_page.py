from .base_page import BasePage
from .locators_for_ali import ProductPageLocators


class ProductPage(BasePage):
    def goods_has_picture_and_description(self):
        picture = self.browser.find_element(*ProductPageLocators.PRODUCT_PICTURE)
        description = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text
        assert description != ''

    def button_add_to_basket_is_represented_on_page(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)