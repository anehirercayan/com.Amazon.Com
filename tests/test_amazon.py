import time
import unittest

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestAmazonAddToCart(BaseTest):
    def testAmazonAddToCart(self):
        home_page = HomePage(self.driver)
        #Amazon sayfasına gidildiği doğrulanır
        self.assertEqual(self.base_url, home_page.get_current_url(), "Amazon Anasayfası Açılmadı.")

        home_page = HomePage(self.driver)
        # açılan pop-up reddete basılarak kapatılır
        home_page.pop_up_reject()
        # search box ta samsung yazısı yazılarak arama yapılır
        home_page.search()
        home_page.send_keys_samsung("samsung")

        category_page = CategoryPage(self.driver)
        self.assertIn(CategoryPage.search_text, category_page.verify_search_results(),  "Aranan ürün sonuçları listeye eklenmedi veya ürün aranamadı")
        time.sleep(2)
        # ikinci sayfa butonuna tıklanır
        category_page.click_second_page()
        time.sleep(2)
        # ikinci sayfada olunduğu doğrulanır
        category_page.verify_second_page()
        time.sleep(2)
        # ürüne tıklanir
        category_page.click_product()

        product_page = ProductPage(self.driver)
        # ürün sayfasında olunduğu doğrulanır
        self.assertTrue(product_page.is_add_to_cart_present(), "Product sayfasında değilsin")
        time.sleep(2)
        # sepete ekle butonuna tıklanır
        product_page.click_add_to_cart_button()
        time.sleep(2)

        cart_page = CartPage(self.driver)
        # sepet ürünün eklendiği doğrulanır
        self.assertIn(cart_page.cart_header_text, cart_page.is_cart_text_present(), "Ürün Sepete Eklenemedi.")
        time.sleep(3)
        # amazon logosuna tıklanır
        cart_page.click_amazon_logo()