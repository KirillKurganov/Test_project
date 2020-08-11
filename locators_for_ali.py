from selenium.webdriver.common.by import By

class MainPageLocators():
    BUTTON_LANGUAGE = (By.CSS_SELECTOR,'#switcher-info .language_txt')
    TEXT_CATEGORIES = (By.CSS_SELECTOR,"div.categories-content-title span")
    BUTTON_AUTHORIZATION = (By.CSS_SELECTOR,'.account-unsigned')
    TEXT_FOR_CHECK_1 = (By.CSS_SELECTOR,'.cl-item-women a')
    TEXT_FOR_CHECK_2 = (By.CSS_SELECTOR,'.cl-item-shoes a')
    TEXT_FOR_CHECK_3 = (By.CSS_SELECTOR,'#home-best-match-area div.title')
    DEUTSCH_LANGUAGE = (By.CSS_SELECTOR,"a.switcher-item[data-site='deu']")
    RUSSIAN_LANGUAGE = (By.CSS_SELECTOR,".switcher-item[data-site='rus']")
    APPLICATION_FOR_ANDROID = (By.CSS_SELECTOR,'a.android-link')
    APPLICATION_FOR_IOS = (By.CSS_SELECTOR,'a.iphone-link')
    SEARCH_FIELD = (By.CSS_SELECTOR,'#search-key')
    SEARCH_RESULT = (By.CSS_SELECTOR,"span[aria-current='page'] span")

class ProductPageLocators():
    PRODUCT_PICTURE = (By.CSS_SELECTOR,'div.magnifier-cover')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR,'h1.product-title-text')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR,"button.addcart[ type='button']")

class LoginPageLoators():
    INPUT_EMAIL = (By.CSS_SELECTOR,'#fm-login-id')
    INPUT_PASSWORD = (By.CSS_SELECTOR,'#fm-login-password')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR,".fm-button[type='submit']")
    BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR,'a.fm-forget')
    PART_SIGN_IN = (By.CSS_SELECTOR,'li.fm-tabs-tab.active')
    ERROR_MESSAGE = (By.CSS_SELECTOR,'span.fm-error-message')
    BUTTON_GOOGLE = (By.CSS_SELECTOR,'a.google')
    BLOCK_REGISTRATION = (By.CSS_SELECTOR,'ul li.fm-tabs-tab')
    REG_EMAIL = (By.CSS_SELECTOR,"input[placeholder='Email address']")
    REG_PASSWORD = (By.CSS_SELECTOR,".fm-field input[type='password']")
    REG_BUTTON = (By.CSS_SELECTOR,"button.fm-button[type='submit']")
    PROFILE_GREETING = (By.CSS_SELECTOR,"span[data-role='username']")




