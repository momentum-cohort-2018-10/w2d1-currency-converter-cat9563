from currency import convert_same_currency
rates = []

def test_convert_same_currency():
    assert convert_same_currency(rates, 12, current = "e", to = "e") == 12
    assert convert_same_currency(rates, 11, current = "e", to = "e") == 11