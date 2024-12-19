from pages.base_page import BasePage
from pages.locators import cart_locator as loc
from playwright.sync_api import expect

class Cart(BasePage):
    page_url = '/28/krossovki-bug/'

    def cart_add_product(self):
        button = self.find(loc.button_add_to_cart_locator)
        button.click()

    def check_name_product(self, product):
        expect(self.find(loc.name_product_locator)).to_have_text(product)

    def check_indicator(self, number: int):
        expect(self.find(loc.indicator_nuber_locator)).to_have_text(str(number))

