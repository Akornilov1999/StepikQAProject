import pytest, time
from selenium.webdriver.common.by import By
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link'
	,["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(number)
	if number != 7
	else pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(number), marks=pytest.mark.xfail)
	for number in range(0, 10)])
def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	time.sleep(1)
	page.should_be_product_name()
	page.should_be_product_price()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()


@pytest.mark.parametrize('should_basket_be_empty', [True, False])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, should_basket_be_empty):
	if not should_basket_be_empty:
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
		page = ProductPage(browser, link)
		page.open()
		page.add_product_to_basket()
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket_page()
	page = BasketPage(browser, browser.current_url)
	page.should_be_empty_basket() if should_basket_be_empty else page.should_not_be_empty_basket()
