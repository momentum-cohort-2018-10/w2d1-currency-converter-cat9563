import pytest
from currency import convert

def test_convert_same_currency():
    assert convert([], 12, current = "USD", to = "USD") == 12
    assert convert([], 11, current = "USD", to = "USD") == 11

def test_convert_forward():
    assert convert(
        rates=[("USD", "EUR", 0.74)], value=1, current='USD', to='EUR') == 0.74
    assert round(
        convert(
            rates=[("USD", "EUR", 0.74)], value=3, current='USD', to='EUR'),
        2) == 2.22

def test_convert_reveres():
   assert round(
        convert(
            rates=[("USD", "EUR", 0.74)], value=1, current='EUR', to='USD'),
        2) == 1.35
