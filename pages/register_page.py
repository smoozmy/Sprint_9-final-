import allure
from locators.register_page_locators import RegisterPageLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_element_visible(HeaderLocators.CREATE_ACCOUNT_BUTTON).click()
        self.wait_element_visible(RegisterPageLocators.FIRST_NAME_INPUT)

    @allure.step("Заполнение формы регистрации")
    def fill_registration_form(self, user):
        self.wait_element_visible(RegisterPageLocators.FIRST_NAME_INPUT).send_keys(user["first_name"])
        self.wait_element_visible(RegisterPageLocators.LAST_NAME_INPUT).send_keys(user["last_name"])
        self.wait_element_visible(RegisterPageLocators.USERNAME_INPUT).send_keys(user["username"])
        self.wait_element_visible(RegisterPageLocators.EMAIL_INPUT).send_keys(user["email"])
        self.wait_element_visible(RegisterPageLocators.PASSWORD_INPUT).send_keys(user["password"])

    @allure.step("Завершение регистрации, переход на страницу авторизации")
    def click_create_account_button(self):
        self.wait_element_visible(RegisterPageLocators.CREATE_ACCOUNT_BUTTON).click()
        return LoginPage(self.driver)