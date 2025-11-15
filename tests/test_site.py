
import time
from pages.homepage import HomePage
from  pages.product import ProductPage
from pages.monitor import MonitorPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxys6()
    product_page = ProductPage(driver)
    product_page.check_tittle_is("Samsung galaxy s6")

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitors()
    time.sleep(2) #исправлю как научусь
    monitor_page = MonitorPage(driver)
    monitor_page.check_monitor_count_is(2)