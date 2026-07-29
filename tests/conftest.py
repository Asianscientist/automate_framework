import pytest
from pages import LoginPage, InventoryPage

@pytest.fixture
def logged_in_page(page):
    LoginPage(page).login("standard_user", "secret_sauce")
    return InventoryPage(page)


