import allure

from src.helpers import Helpers
from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage


class RecipePage(BasePage):

    @allure.step("Проверка отображения рецепта на странице")
    def assert_recipe_created(self, expected_recipe):
        actual_name = self.wait_element_visible(RecipePageLocators.NAME).text
        actual_description = self.wait_element_visible(RecipePageLocators.DESCRIPTION).text

        for key in expected_recipe["ingredients"].keys():
            self.wait_until(
                lambda d: any(key in el.text for el in d.find_elements(*RecipePageLocators.INGREDIENTS)),
                timeout=10,
                error_msg=f"Ингредиент '{key}' не загрузился вовремя"
            )

        actual_ingredients = self.find_elements(RecipePageLocators.INGREDIENTS)
        ingredients = [
            el.text.replace('–', '-').replace('—', '-').strip()
            for el in actual_ingredients
        ]

        assert actual_name == expected_recipe["name"]
        assert actual_description == expected_recipe["description"]

        for key, value in expected_recipe["ingredients"].items():
            assert Helpers.is_substr_in_list(f"{key} - {value}", ingredients)
