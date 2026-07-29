import os
import pytest
import allure
from pages import LoginPage, InventoryPage

@pytest.fixture
def logged_in_page(page):
    LoginPage(page).login("standard_user", "secret_sauce")
    return InventoryPage(page)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=path)
        allure.attach.file(path, name="failure", attachment_type=allure.attachment_type.PNG)