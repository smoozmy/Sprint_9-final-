from selenium.webdriver.common.by import By


class MenuLocators:
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/signup']")
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/signin']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    RECIPES_BUTTON = (By.XPATH, "//a[contains(text(),'Рецепты')]")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//a[@href='/recipes/create']")