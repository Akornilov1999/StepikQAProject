import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.firefox.options import Options as Firefox_options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="ru",
		help="Choose user_language: en, ru, etc")
	parser.addoption('--browser_name', action='store', default="chrome",
		help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	browser_name = request.config.getoption("browser_name")
	browser = None
	if browser_name == "chrome":
		options = Chrome_options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		print("\nstart chrome browser for test..")
		browser = webdriver.Chrome(options=options)
	elif browser_name == "firefox":
		options = Firefox_options()
		options.set_preference("intl.accept_languages", user_language)
		print("\nstart firefox browser for test..")
		browser = webdriver.Firefox(options=options)
	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")
	yield browser
	print("\nquit browser..")
	browser.quit()
