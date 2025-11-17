from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def check_tittle_is(self, tittle):
        page_tittle = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert page_tittle.text == "Samsung galaxy s6"