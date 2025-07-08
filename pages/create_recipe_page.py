from pathlib import Path
import allure
from selenium.common.exceptions import StaleElementReferenceException
from src.data import Data
from locators.create_recipe_locators import CreateRecipeLocators
from pages.base_page import BasePage
from pages.recipe_page import RecipePage


class CreateRecipePage(BasePage):

    @allure.step('Переход к странице рецепта')
    def to_recipe_page(self):
        return RecipePage(self.driver)

    @allure.step('Заполнение формы рецепта')
    def fill_form(self, recipe):
        self.wait_element_visible(CreateRecipeLocators.NAME).send_keys(recipe["name"])
        self.__check_and_set_tag__(recipe["tags"])
        self.__add_ingredients(recipe["ingredients"])
        self.wait_element_visible(CreateRecipeLocators.COOK_TIME).send_keys(recipe["cook_time"])
        self.wait_element_visible(CreateRecipeLocators.DESCRIPTION).send_keys(recipe["description"])
        self.__add_photo__(recipe["photo"])
        self.wait_element_visible(CreateRecipeLocators.PHOTO_PREVIEW)

    @allure.step("Завершение создания рецепта")
    def submit_form(self):
        button = self.wait_element_visible(CreateRecipeLocators.CREATE_RECIPE_BUTTON)

        if not button.is_enabled():
            raise Exception("Кнопка создания рецепта неактивна")

        if not button.is_displayed():
            self.scroll_to_element(button)
            self.wait_until_clickable(CreateRecipeLocators.CREATE_RECIPE_BUTTON)

        try:
            button.click()
        except:
            self.click_with_js(CreateRecipeLocators.CREATE_RECIPE_BUTTON)

    @allure.step("Добавить ингредиенты")
    def __add_ingredients(self, ingredients):
        for name, amount in ingredients.items():
            self.type_ingredient_name(name)
            self.type_ingredient_amount(amount)
            self.wait_element_visible(CreateRecipeLocators.INGREDIENT_ADD_LINK).click()

    @allure.step("Изменить ингредиенты")
    def type_ingredient_name(self, name):
        self.wait_element_visible(CreateRecipeLocators.INGREDIENT_NAME).send_keys(name)
        self.wait_element_visible(CreateRecipeLocators.INGREDIENT_LIST)

        elements = self.find_elements(CreateRecipeLocators.INGREDIENT_LIST)
        for _ in range(3):
            try:
                for element in elements:
                    if element.text == name:
                        element.click()
                        return
                break
            except StaleElementReferenceException:
                elements = self.find_elements(CreateRecipeLocators.INGREDIENT_LIST)


    def type_ingredient_amount(self, amount):
        self.wait_element_visible(CreateRecipeLocators.INGREDIENT_AMOUNT).send_keys(amount)

    @allure.step("Обозначить время приема")
    def __check_and_set_tag__(self, expected_tags):
        for tag in Data.EAT_TAGS:
            tag_element = self.wait_element_visible(self.__get_tag_by_name__(tag))
            tag_clicked = "checkbox_active" in tag_element.get_attribute("class")
            if tag in expected_tags:
                if not tag_clicked:
                    tag_element.click()
            else:
                tag_element.click()
    @allure.step("Добавить фото к рецепту")
    def __add_photo__(self, photo):
        file_path = str(Path(__file__).parent.parent) + "/assets/" + photo
        self.find_element(CreateRecipeLocators.UPLOAD_PHOTO_INPUT).send_keys(file_path)


    def __get_tag_by_name__(self, tag: str):
        if tag.lower() == "breakfast":
            return CreateRecipeLocators.BREAKFAST_BUTTON
        elif tag.lower() == "lunch":
            return CreateRecipeLocators.LUNCH_BUTTON
        else:
            return CreateRecipeLocators.DINNER_BUTTON