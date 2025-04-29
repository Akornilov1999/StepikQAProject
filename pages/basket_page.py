from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
	def should_be_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"

	def should_not_be_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket is empty"
