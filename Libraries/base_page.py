from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Libraries.video_page.locators import MainPageLocators


class BasePage(MainPageLocators):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def scroll_to_element(self, locator):
        self.driver.execute_script("argument[0].scrollIntoView();", locator)

    def element(self, locator, timeout=10):
        return (WebDriverWait(self.driver, timeout)
                .until(EC.presence_of_element_located(locator)
                       ))

    def element_is_visible(self, locator, timeout=10):
        return (WebDriverWait(self.driver, timeout)
                .until(EC.visibility_of_element_located(locator)
                       ))

    def element_is_clickable(self, locator, timeout=10):
        return (WebDriverWait(self.driver, timeout)
                .until(EC.element_to_be_clickable(locator)
                       ))

    def elements(self, locator):
        elements = (WebDriverWait(self.driver, 10)
                    .until(EC.visibility_of_all_elements_located(locator)
                           ))
        return elements
