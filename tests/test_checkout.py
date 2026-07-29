from pages import CartPage

def test_full_checkout(logged_in_page):
    logged_in_page.add_to_cart()
    logged_in_page.page.click(".shopping_cart_link")

    cart = CartPage(logged_in_page.page)
    cart.checkout()
    cart.fill_info("Jane", "Doe", "94107")
    cart.finish()

    assert cart.complete_text() == "Thank you for your order!"