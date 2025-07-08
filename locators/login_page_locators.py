from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT  = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, "//button")
    TITLE = (By.XPATH, "//h1[starts-with(@class,'styles_title')]")