from pages import LoginPage
import pytest

def test_valid_login(page):
    LoginPage(page).login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url

def test_invalid_login_shows_error(page):
    lp = LoginPage(page)
    lp.login("standard_user", "wrong_pass")
    assert "do not match" in lp.error_text()

@pytest.mark.parametrize("username,password,expected", [
    ("bad_user", "secret_sauce", "do not match"),
    ("standard_user", "wrong_pass", "do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
])
def test_invalid_login(page, username, password, expected):
    lp = LoginPage(page)
    lp.login(username, password)
    assert expected in lp.error_text()