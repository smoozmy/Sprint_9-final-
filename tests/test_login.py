import allure

@allure.epic('Авторизация')
class TestLogin:

    @allure.title("Регистрация и последующий логин")
    def test_login(self, register_page, new_user):
        register_page.fill_registration_form(new_user)
        login_page = register_page.click_create_account_button()
        login_page.fill_form_and_login(new_user)
        login_page.assert_user_logged_in()
