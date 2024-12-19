from pages.locators import category_locator as loc
from pages.base_page import BasePage
from playwright.sync_api import expect

class Category(BasePage):
    page_url = '/27/snoubord-burton-faang/'

    def category_snowbord(self):
        category_name = self.find(loc.name_category_locator)
        category_name.click()

    def check_name_category(self, category):
        expect(self.find(loc.category_page_locator)).to_have_text(category)
