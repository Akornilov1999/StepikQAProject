import pytest
from selenium.webdriver.common.by import By
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()

def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.parametrize('should_basket_be_empty', [True, False])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, should_basket_be_empty):
	if not should_basket_be_empty:
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_basket()
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link)
	page.open()
	page.go_to_basket_page()
	page = BasketPage(browser, browser.current_url)
	page.should_be_empty_basket() if should_basket_be_empty else page.should_not_be_empty_basket()
