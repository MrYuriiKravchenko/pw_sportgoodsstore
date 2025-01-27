from playwright.sync_api import Page, Locator

class BasePage:
    base_url = 'https://www.sportgoodsstore.ru'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url is not None:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page not open')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)
