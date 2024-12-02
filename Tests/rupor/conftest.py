import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def url():
    return "https://platform.rupor-test.rutube.dev"