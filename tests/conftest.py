import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.data import Data
from pages.register_page import RegisterPage
from src.generators import Generators
from pages.recipes_page import RecipesPage
import os


@pytest.fixture()
def driver():
    if os.getenv('IN_CONTAINER') == 'true':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("browserVersion", "124.0")
        chrome_options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })
        driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            options=chrome_options
        )
    else:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

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


@pytest.fixture(scope='function')
def authorized_user_recipes_page(register_page, driver):
    user = {
        "first_name": "T" + Generators.generate_text(14),
        "last_name": "B" + Generators.generate_text(14),
        "username": "user" + Generators.generate_text(14),
        "email": Generators.generate_email(),
        "password": Data.PASSWORD,
    }

    register_page.fill_registration_form(user)
    login_page = register_page.click_create_account_button()

    login_page.fill_form_and_login(user)

    return RecipesPage(driver)

