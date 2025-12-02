from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def visit(self, url):
        self.driver.get(url)

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        elem = self.find(locator)
        elem.click()

    def type(self, locator, text, clear_first=True):
        elem = self.find(locator)
        if clear_first:
            elem.clear()
        elem.send_keys(text)

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False
