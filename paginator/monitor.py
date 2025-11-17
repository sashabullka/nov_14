from selenium.webdriver.common.by import By


class MonitorPage:

    def __init__(self, driver):
        self.driver = driver

    def check_monitor_count_is(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count