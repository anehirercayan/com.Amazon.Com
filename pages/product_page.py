from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_ICON = By.XPATH, "(// *[@ id='add-to-cart-button'])[1]"

    def is_add_to_cart_present(self):
        return self.find(*self.ADD_TO_CART_ICON)

    def click_add_to_cart_button(self):
        self.click_element(*self.ADD_TO_CART_ICON)
