class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.goto("https://www.saucedemo.com")
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def error_text(self):
        return self.page.locator("[data-test='error']").inner_text()


class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, item_text="Add to cart"):
        self.page.click(f"text={item_text}")

    def cart_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()

        