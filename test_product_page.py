import pytest, time
from selenium.webdriver.common.by import By
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.login_guest
class TestGuestAddToBasketFromProductPage():
	@pytest.mark.need_review
	@pytest.mark.xfail
	def test_guest_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_basket()
		time.sleep(1)
		page.should_be_product_name()
		page.should_be_product_price()

	@pytest.mark.skip
	def test_guest_should_see_login_link_on_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.should_be_login_link()

	@pytest.mark.need_review
	def test_guest_can_go_to_login_page_from_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.go_to_login_page()

	@pytest.mark.need_review
	def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_basket()
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = ProductPage(browser, link)
		page.open()
		page.go_to_basket_page()
		page = BasketPage(browser, browser.current_url)
		page.should_not_be_empty_basket()

@pytest.mark.negative_basket
class TestNegativeBasket():
	@pytest.mark.xfail
	@pytest.mark.skip
	def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link, 0)
		page.open()
		page.add_product_to_basket()
		page.should_not_be_success_message()

	@pytest.mark.skip
	def test_guest_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link, 0)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.xfail
	@pytest.mark.skip
	def test_message_disappeared_after_adding_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link, 0)
		page.open()
		page.add_product_to_basket()
		page.message_should_be_disappeared()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "https://selenium1py.pythonanywhere.com/accounts/login/"
		page = LoginPage(browser, link)
		page.open()
		mail = str(time.time()) + "@fakemail.org"
		password = str(time.time()) + "qWERTy" + str(time.time())
		page.register_new_user(mail, password)
		page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_basket()
		time.sleep(1)
		page.should_be_product_name()
		page.should_be_product_price()

	@pytest.mark.skip
	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link, 0)
		page.open()
		page.should_not_be_success_message()
