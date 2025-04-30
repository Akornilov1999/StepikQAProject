from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class BasketPageLocators():
	EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > :nth-child(1) > a")
	NOT_EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-title")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
	PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1) .alertinner > strong")
	PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1) .alertinner > strong")
