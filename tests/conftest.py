import pytest
import chromedriver_autoinstaller
from selenium import webdriver


@pytest.fixture()
def driver():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
