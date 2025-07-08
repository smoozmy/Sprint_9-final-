import allure

from pages.recipe_page import RecipePage
from src.data import Data

@allure.epic('Рецепты')
class TestRecipes:

    @allure.title("Создание нового рецепта")
    def test_recipes(self, authorized_user_recipes_page):
        recipes_page = authorized_user_recipes_page
        create_recipe_page = recipes_page.open_new_recipe()

        recipe = Data.RECIPE
        create_recipe_page.fill_form(recipe)
        create_recipe_page.submit_form()

        recipe_page = create_recipe_page.to_recipe_page()
        recipe_page.assert_recipe_created(recipe)
