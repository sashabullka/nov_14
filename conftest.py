import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from paginator.homepage import HomePage
from paginator.product import ProductPage
from paginator.monitor import MonitorPage

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get('https://demoblaze.com/index.html')
    yield driver
    driver.close()

@pytest.fixture
def pages(driver):
    class Pages:
        def __init__(self, driver):
            self.home = HomePage(driver)
            self.product = ProductPage(driver)
            self.monitor = MonitorPage(driver)
    
    return Pages(driver)