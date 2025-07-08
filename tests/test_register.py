import allure

@allure.epic('Регистрация')
class TestRegister:

    @allure.title("Регистрация нового пользователя")
    def test_registration(self, new_user, register_page):
        register_page.fill_registration_form(new_user)
        register_page.click_create_account_button()

