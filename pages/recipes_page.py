import allure
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from pages.create_recipe_page import CreateRecipePage


class RecipesPage(BasePage):

    @allure.step("Переход к созданию нового рецепта")
    def open_new_recipe(self):
        self.wait_element_visible(HeaderLocators.CREATE_RECIPE_BUTTON).click()
        return CreateRecipePage(self.driver)