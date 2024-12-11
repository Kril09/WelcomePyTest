import pytest

from selenium import webdriver

from Libraries.video_page.constants import BASE_URL
from Libraries.video_page.video_page import VideoPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def url():  # базовый URL
    return BASE_URL


@pytest.fixture(scope="function")
def video_page(driver, url):
    """Создание экземпляра VideoPage для тестов."""
    return VideoPage(driver=driver, url=url)
