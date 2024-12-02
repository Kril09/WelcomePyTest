from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def scroll_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def el_is_visible(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def el_is_clickable(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def el_is_visible_all(self, selection):
        elements = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(selection)
        )
        return elements
