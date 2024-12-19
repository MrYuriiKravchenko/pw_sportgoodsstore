from pages.locators import filter_locator as loc
from pages.base_page import BasePage
from playwright.sync_api import expect


class FilterPrice(BasePage):
    page_url = ''

    def choice_filter(self):
        filter_price = self.find(loc.select_locator)
        filter_price.select_option('По убыванию цены')
        filter_price.click()

    def button_filter(self):
        button = self.find(loc.button_filter_locator)
        button.click()

    def check_that_the_price_is_in_descending_order(self, price):
        expect(self.find(loc.product_price_low)).to_have_text(price)

