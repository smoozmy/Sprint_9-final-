import allure

from src.helpers import Helpers
from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage


class RecipePage(BasePage):

    @allure.step("Проверка отображения рецепта на странице")
    def assert_recipe_created(self, expected_recipe):
        actual_name = self.wait_element_visible(RecipePageLocators.NAME).text
        actual_description = self.wait_element_visible(RecipePageLocators.DESCRIPTION).text
        actual_ingredients = self.driver.find_elements(*RecipePageLocators.INGREDIENTS)
        ingredients = []
        for ingredient in actual_ingredients:
            ingredients.append(ingredient.text)
        assert actual_name == expected_recipe["name"]
        assert actual_description == expected_recipe["description"]
        for key, value in expected_recipe["ingredients"].items():
            assert Helpers.is_substr_in_list(f"{key} - {value}", ingredients)