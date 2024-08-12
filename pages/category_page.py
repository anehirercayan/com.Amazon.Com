from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CategoryPage(BasePage):
    SEARCH_RESULTS_TEXT = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    search_text = "samsung"
    SECOND_PAGE_BUTTON=(By.CSS_SELECTOR, ".s-pagination-next")
    SECOND_PAGE_SELECTED= (By.CSS_SELECTOR, ".s-pagination-item.s-pagination-selected")
    DESIRED_PRODUCT= (By.XPATH, "(//div[@data-component-type='s-search-result'])[(5 - 1) * 4 + 1]")

    def verify_search_results(self):
        return self.get_text(self.SEARCH_RESULTS_TEXT)

    def click_second_page(self):
        element = self.find(*self.SECOND_PAGE_BUTTON)
        self.scroll_into_view(self.SECOND_PAGE_BUTTON)  # Öğeye kaydırma yapar
        self.click_element(*self.SECOND_PAGE_BUTTON)  # Öğeye tıklar

    def verify_second_page(self):
        element = self.find(*self.SECOND_PAGE_SELECTED)
        self.scroll_into_view(self.SECOND_PAGE_SELECTED)  # Öğeye kaydırma yapar

    def click_product(self):
        element = self.click_element(*self.DESIRED_PRODUCT)



