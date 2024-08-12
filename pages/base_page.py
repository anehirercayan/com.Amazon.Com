from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, search_text):
        element = self.find(*locator)
        element.send_keys(search_text)
        #Metni yazar

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        element = self.wait_element(locator)
        return element.text

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def scroll_into_view(self, locator):
        #Belirtilen öğeyi görünür yapacak şekilde kaydırır.
        element = self.find(*locator)
        self.execute_script("arguments[0].scrollIntoView(true);", element)