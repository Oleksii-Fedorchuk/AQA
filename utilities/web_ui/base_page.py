from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_elements_located(self, locator):
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        element = self._wait_until_clickable(locator)
        element.click()

    def read_text(self, locator):
        return self._wait_until_element_visible(locator).text

    def get_image(self, locator):
        return self._wait_until_element_located(locator)

    def current_url(self):
        return self._driver.current_url

    def current_title(self):
        return self._driver.title
