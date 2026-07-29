def test_valid_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    assert "inventory.html" in page.url


def test_invalid_login_shows_error(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_pass")
    page.click("#login-button")

    error_text = page.locator("[data-test='error']").inner_text()
    assert "do not match" in error_text