from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
	def add_product_to_basket(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_to_basket_button.click()
		self.solve_quiz_and_get_code()

	def should_be_product_name(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
		product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
		assert product_name.text == product_name_in_message.text, "Product name doesn't match"

	def should_be_product_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
		assert product_price.text == product_price_in_message.text, "Product price doesn't match"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def message_should_be_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
