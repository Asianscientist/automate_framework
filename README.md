# SauceDemo Test Automation Framework

A UI test automation framework for [SauceDemo](https://www.saucedemo.com), built with **Playwright**, **Pytest**, and the **Page Object Model**, with **Allure reporting**, **automatic screenshots on failure**, **parallel test execution**, **Docker**, and a **GitHub Actions CI pipeline**.

## Stack

| Tool | Purpose |
|---|---|
| Playwright | Browser automation |
| Pytest | Test runner |
| Page Object Model | Separates page structure/locators from test logic |
| Allure | Test reporting |
| pytest-xdist | Parallel test execution |
| pytest-rerunfailures | Auto-retry of flaky tests |
| Docker | Containerized, reproducible test runs |
| GitHub Actions | CI on every push/PR |

## Project structure

```
qa-framework/
├── tests/
│   ├── pages.py            
│   ├── conftest.py          
│   ├── test_login.py         
│   ├── test_cart.py         #
│   ├── test_checkout.py     # 
│   └── test_sort.py         # 
├── explore.py               #
├── pytest.ini                
├── requirements.txt
├── Dockerfile
├── .github/workflows/tests.yml
├── allure-results/          
└── screenshots/             
```

## Test coverage

- **Login**: valid login, invalid username/password, empty-field validation, locked-out user
- **Cart**: add item, remove item, cart badge count
- **Checkout**: full end-to-end order flow
- **Product sorting**: price low→high, name A→Z/Z→A (used in place of a search feature, since SauceDemo doesn't have a free-text search bar — see note below)

## Setup

```bash
git clone <this-repo>
cd qa-framework
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### A note on scope

SauceDemo is a deliberately minimal demo app — it has no self-service registration form and no free-text search bar. Rather than fabricate tests against features that don't exist, this framework demonstrates the equivalent patterns using what the app actually offers (empty-field validation in place of registration validation; sort/filter in place of search). Retargeting the framework at an app with those features is a matter of adding one new Page Object class and updating locators — the rest of the framework (fixtures, reporting, CI, Docker) doesn't change.
