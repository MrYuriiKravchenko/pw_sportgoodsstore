def test_filter_price(filter_price):
    filter_price.open_page()
    filter_price.choice_filter()
    filter_price.button_filter()
    filter_price.check_that_the_price_is_in_descending_order('₽ 992132,00')
