def test_sort_price_low_to_high(logged_in_page):
    logged_in_page.sort_by("lohi")
    prices = logged_in_page.prices()
    assert prices == sorted(prices)

    