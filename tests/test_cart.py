def test_cart_add_product(cart):
    cart.open_page()
    cart.cart_add_product()
    cart.check_name_product('Кроссовки Bug')
    cart.check_indicator(1)
