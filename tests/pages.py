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

    def remove_from_cart(self, item_text="Remove"):
        self.page.click(f"text={item_text}")

    def cart_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()
    
    def sort_by(self, value):
        self.page.select_option(".product_sort_container", value)

    def prices(self):
        raw = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]

class CartPage:
    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.click("#checkout")

    def fill_info(self, first, last, zip_code):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")

    def finish(self):
        self.page.click("#finish")

    def complete_text(self):
        return self.page.locator(".complete-header").inner_text()