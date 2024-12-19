import pytest
from pages.search import SearchProduct
from pages.cart import Cart
from pages.filter import FilterPrice
from pages.category import Category

@pytest.fixture()
def filter_price(page):
    return FilterPrice(page)

@pytest.fixture()
def search_product(page):
    return SearchProduct(page)

@pytest.fixture()
def cart(page):
    return Cart(page)

@pytest.fixture()
def category(page):
    return Category(page)
