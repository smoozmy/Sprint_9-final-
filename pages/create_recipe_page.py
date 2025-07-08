import time
from pathlib import Path

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Data
from locators.create_recipe_locators import CreateRecipeLocators
from pages.base_page import BasePage
from pages.recipe_page import RecipePage


class CreateRecipePage(BasePage):
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
            self.driver.execute_script("arguments[0].scrollIntoView();", button)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreateRecipeLocators.CREATE_RECIPE_BUTTON)
        )

        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)

        return RecipePage(self.driver)

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
        elements = self.driver.find_elements(*CreateRecipeLocators.INGREDIENT_LIST)
        for element in elements:
            if element.text == name:
                element.click()
                break


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
        self.driver.find_element(*CreateRecipeLocators.UPLOAD_PHOTO_INPUT).send_keys(file_path)


    def __get_tag_by_name__(self, tag: str):
        if tag.lower() == "breakfast":
            return CreateRecipeLocators.BREAKFAST_BUTTON
        elif tag.lower() == "lunch":
            return CreateRecipeLocators.LUNCH_BUTTON
        else:
            return CreateRecipeLocators.DINNER_BUTTON