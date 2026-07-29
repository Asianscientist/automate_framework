def test_add_item_to_cart(logged_in_page):
    logged_in_page.add_to_cart()
    assert logged_in_page.cart_count() == "1"