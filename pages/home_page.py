from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    search_text = "samsung"
    POP_UP_REJECT_BUTTON = (By.XPATH, "//span[@class='a-button-inner']//*[text()='Reddet']")

    def pop_up_reject (self):
        self.click_element(*self.POP_UP_REJECT_BUTTON)

    def search(self):
        # Arama alanını bul
        self.find(*self.SEARCH_BOX)
        self.click_element(*self.SEARCH_BOX)
        
    def send_keys_samsung(self, search_text):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)
