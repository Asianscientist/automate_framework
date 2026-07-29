FROM mcr.microsoft.com/playwright/python:v1.47.0-jammy
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "-n", "auto", "--alluredir=allure-results"]


"""
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -r requirements.txt && playwright install --with-deps chromium
      - run: pytest -n auto --alluredir=allure-results
      - uses: actions/upload-artifact@v4
        if: always()
        with: { name: allure-results, path: allure-results }
"""