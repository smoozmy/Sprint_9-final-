import allure
from src.data import Data

@allure.epic('Рецепты')
class TestRecipes:

    @allure.title("Создание нового рецепта")
    def test_recipes(self, authorized_user_recipes_page):
        recipes_page = authorized_user_recipes_page

        create_recipe_page = recipes_page.open_new_recipe()

        recipe = Data.get_recipe()
        create_recipe_page.fill_form(recipe)
        recipe_page = create_recipe_page.submit_form()

        recipe_page.assert_recipe_created(recipe)