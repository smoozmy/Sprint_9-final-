from selenium.webdriver.common.by import By


class CreateRecipeLocators:
    NAME  = (By.XPATH,"//div[text()='Название рецепта']/parent::label/input")
    BREAKFAST_BUTTON  = (By.XPATH,"//span[text()='Завтрак']/parent::div/button")
    LUNCH_BUTTON  = (By.XPATH,"//span[text()='Обед']/parent::div/button")
    DINNER_BUTTON  = (By.XPATH,"//span[text()='Ужин']/parent::div/button")
    INGREDIENT_NAME  = (By.XPATH,"//div[starts-with(@class, 'styles_ingredientsInputs')]//input")
    INGREDIENT_AMOUNT  = (By.XPATH,"//div[starts-with(@class, 'styles_ingredientsAmountInputContainer')]//input")
    INGREDIENT_LIST  = (By.XPATH,"//div[starts-with(@class, 'styles_ingredientsInputs')]/div[starts-with(@class, 'styles_container')]/div")
    INGREDIENT_ADD_LINK  = (By.XPATH,"//div[starts-with(@class, 'styles_ingredientAdd')]")
    COOK_TIME  = (By.XPATH,"//div[text()='Время приготовления']/parent::label/input")
    DESCRIPTION  = (By.XPATH,"//textarea")
    UPLOAD_PHOTO_INPUT = (By.XPATH,"//input[starts-with(@class, 'styles_fileInput')]")
    UPLOAD_PHOTO_BUTTON = (By.XPATH,"//div[starts-with(@class, 'styles_button')]")
    CREATE_RECIPE_BUTTON = (By.XPATH,"//button[contains(text(),'Создать рецепт')]")
    PHOTO_PREVIEW = (By.XPATH, "//div[contains(@class, 'styles_image')]")