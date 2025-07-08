from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 5):
        self.driver = driver
        self.timeout = timeout

    def wait_element_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def wait_element_visible_custom_duration(self, locator, seconds):
        return WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(locator))

    def wait_element_not_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(locator))

    def wait_element_has_text(self, locator, text):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element(locator, str(text)))

    def wait_util_element_text_changes(self, locator, text):
        return WebDriverWait(self.driver, self.timeout).until(
            lambda drv: drv.find_element(*locator).text != str(text))

    def format_locator(self, locator, text):
        new_locator = (locator[0], locator[1].format(text))
        return new_locator

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def wait_until(self, condition_function, timeout=None, error_msg="Состояние не выполнено"):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        try:
            return wait.until(condition_function)
        except Exception as e:
            raise AssertionError(f"{error_msg}: {e}")
