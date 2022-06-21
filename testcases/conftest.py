from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'Chrome':
       driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default="Chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




















