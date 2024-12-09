from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Libraries.locators import MainPageLocators


class BasePage(MainPageLocators):
    locators = MainPageLocators()

    def __init__(self, driver, url, email, code):
        self.driver = driver
        self.url = url
        self.email = email
        self.code = code

    def open(self):
        self.driver.get(self.url)

    def scroll_to_element(self, locator):
        self.driver.execute_script("argument[0].scrollIntoView();", locator)

    def element_is_visible(self, locator, timeout=10):
        return (WebDriverWait(self.driver, timeout)
                .until(EC.visibility_of_element_located(locator)
                       ))

    def element_is_clickable(self, locator, timeout=10):
        return (WebDriverWait(self.driver, timeout)
                .until(EC.element_to_be_clickable(locator)
                       ))

    def element_is_visible_all(self, locator):
        elements = (WebDriverWait(self.driver, 10)
                    .until(EC.visibility_of_all_elements_located(locator)
                           ))
        return elements

    def auth(self, email, code):  # метод авторизации
        self.element_is_visible(self.BUTTON_AUTH).click()
        self.element_is_clickable(self.INPUT_EMAIL, 10).send_keys(email)
        self.element_is_visible(self.NEXT_BUTTON).click()
        self.element_is_visible(self.INPUT_CODE0).send_keys(code)
