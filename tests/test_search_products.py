
def test_search(search_product):
    search_product.open_page()
    search_product.search_form('Кроссовки Bug')
    search_product.check_found_product('Кроссовки Bug')

