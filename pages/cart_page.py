from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ADDED_TEXT = (By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    cart_header_text = "Sepete Eklendi"
    AMAZON_LOGO = (By.ID, "nav-logo-sprites")

    def is_cart_text_present(self):
        return self.get_text(self.CART_ADDED_TEXT)

    def click_amazon_logo(self):
        self.click_element(*self.AMAZON_LOGO)