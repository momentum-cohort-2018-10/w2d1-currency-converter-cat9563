from currency import convert
rates = []

def test_convert():
    rates = []
    assert convert(rates, 12, form = "e", to = "e") == 12