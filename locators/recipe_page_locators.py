from selenium.webdriver.common.by import By

class RecipePageLocators:
    NAME = (By.XPATH, "//h1[starts-with(@class, 'styles_single-card__title')]")
    COOK_TIME = (By.XPATH, "//p[starts-with(@class, 'styles_single-card__text__2_')]")
    DESCRIPTION = (By.XPATH, "//div[contains(@class, 'styles_description__')]/div")
    INGREDIENTS = (By.XPATH, "//p[starts-with(@class, 'styles_ingredients__list-item')]")