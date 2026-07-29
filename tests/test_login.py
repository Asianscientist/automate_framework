from pages import LoginPage

def test_valid_login(page):
    LoginPage(page).login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url

def test_invalid_login_shows_error(page):
    lp = LoginPage(page)
    lp.login("standard_user", "wrong_pass")
    assert "do not match" in lp.error_text()