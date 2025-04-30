from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
	def register_new_user(self, mail, password):
		new_mail = self.browser.find_element(*LoginPageLocators.NEW_MAIL)
		new_mail.send_keys(mail)
		new_passwords = self.browser.find_elements(*LoginPageLocators.NEW_PASSWORD)
		for new_password in new_passwords:
			new_password.send_keys(password)
		register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
		register_button.click()

	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert 'login' in self.browser.current_url, "Login url is not corrected"

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
