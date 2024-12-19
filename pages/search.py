from pages.locators import search_locator as loc
from pages.base_page import BasePage
from playwright.sync_api import expect

class SearchProduct(BasePage):
    page_url = ''

    def search_form(self, product):
        form_field = self.find(loc.search_field_locator)
        button = self.find(loc.button_locator)
        form_field.fill(product)
        button.click()

    def check_found_product(self, product_result):
        expect(self.find(loc.results_found_locator)).to_have_text(product_result)

