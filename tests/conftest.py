import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from src.data import Data
from pages.register_page import RegisterPage
from src.generators import Generators


@pytest.fixture()
def driver():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(Data.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def new_user():
    return {
        "first_name": "T" + Generators.generate_text(14),
        "last_name": "B" + Generators.generate_text(14),
        "username": "user" + Generators.generate_text(14),
        "email": Generators.generate_email(),
        "password": Data.PASSWORD,
    }

@pytest.fixture()
def register_page(driver):
    return RegisterPage(driver)
