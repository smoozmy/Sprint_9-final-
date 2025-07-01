import allure
from locators.login_page_locators import LoginPageLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Заполнение формы логина")
    def fill_form_and_login(self, user) :
        self.wait_element_visible(LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        self.wait_element_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        self.wait_element_visible(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Проверка успешного входа")
    def assert_user_logged_in(self):
        self.wait_element_visible(HeaderLocators.LOGOUT_BUTTON)
        url = self.driver.current_url
        assert url == 'https://foodgram-frontend-1.prakticum-team.ru/recipes'
        return self
