def test_add_item_to_cart(logged_in_page):
    logged_in_page.add_to_cart()
    assert logged_in_page.cart_count() == "1"

def test_remove_item_from_cart(logged_in_page):
    logged_in_page.add_to_cart()
    logged_in_page.remove_from_cart()
    assert logged_in_page.page.locator(".shopping_cart_badge").count() == 0