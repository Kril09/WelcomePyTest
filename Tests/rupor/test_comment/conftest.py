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
def url():  # базовый URL
    return "https://platform.rupor-test.rutube.dev"


@pytest.fixture
def email():  # email для регистрации
    return "test_testuser1@yandex.ru"


@pytest.fixture
def code():  # проверочный код для регистрации
    return "8080"
