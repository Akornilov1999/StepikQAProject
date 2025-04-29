import pytest, time
from selenium.webdriver.common.by import By
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
