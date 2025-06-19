from selenium.webdriver.common.by import By

class CreateAccountPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, '//input[@name="first_name"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@name="last_name"]')
    USERNAME_INPUT  = (By.XPATH, '//input[@name="username"]')
    EMAIL_INPUT  = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT  = (By.XPATH, '//input[@name="password"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button")