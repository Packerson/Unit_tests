from datetime import datetime

import pytest

from functions import div, analyze_pesel, calculate_vat, hash_password, \
    fizz_buzz, leap_year, word_wrap, lorem_ipsum


@pytest.mark.parametrize("a, b, result", (
        (8, 2, 4),  # 1
        (77, 7, 11),  # 1
        (2.25, 0.25, 9),  # 2
        (99.99, 9, 11.11),  # 2
        ("99.99", "9", 11.11),  # 4
        ("8", 2, 4),  # 4
))
def test_div(a, b, result):
    assert div(a, b) == result


def test_div_raises_zero_division_error():  # 3
    with pytest.raises(ZeroDivisionError):
        div(2, 0)


@pytest.mark.parametrize("pesel, result", (
        ("91030477618", {
            "pesel": "91030477618",
            "valid": True,
            "gender": "male",
            "birth_date": datetime(1991, 3, 4)
        }),
        ("76072212504", {
            "pesel": "76072212504",
            "valid": True,
            "gender": "female",
            "birth_date": datetime(1976, 7, 22)
        }),
        ("55091500911", {
            "pesel": "55091500911",
            "valid": True,
            "gender": "male",
            "birth_date": datetime(1955, 9, 15)
        }),
        ("02323186009", {
            "pesel": "02323186009",
            "valid": True,
            "gender": "female",
            "birth_date": datetime(2002, 12, 31)
        }),
        ("10241019215", {
            "pesel": "10241019215",
            "valid": True,
            "gender": "male",
            "birth_date": datetime(2010, 4, 10)
        }),
        ("99121299999", {
            "pesel": "99121299999",
            "valid": False,
            "gender": "male",
            "birth_date": datetime(1999, 12, 12)
        }),
))
def test_analyze_pesel(pesel, result):
    assert analyze_pesel(pesel) == result


@pytest.mark.parametrize("price, vat_rate, vat_value", (
        (100, 25, 25),
        (50, 10, 5),
        (3.5, 20, 0.7),
))
def test_calculate_vat(price, vat_rate, vat_value):
    assert calculate_vat(price, vat_rate) == vat_value


@pytest.mark.parametrize("password, value", (
        ("ala", None),
        ("alamakota", None),
        ("Alamakota", None),
        ("Alamakota1", None),
        ("K1o!aa2", None),
))
def test_hash_password(password, value):
    assert hash_password(password) is value


@pytest.mark.parametrize("x, value", (
        (15, '12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz'),
        (16, '12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz16'),
        (3, '12Fizz'),
        (5, '12Fizz4Buzz')
))
def test_fizz_buzz(x, value):
    assert fizz_buzz(x) == value


@pytest.mark.parametrize('year, value', (
        (1998, False),
        (2000, True),
        (1600, True),
        (2012, True),
        (1900, False),
        (1860, True)
))
def test_leap_year(year, value):
    assert leap_year(year) == value


@pytest.mark.parametrize('text, value, result', (
        (lorem_ipsum, 5, "Lorem..."),
        (lorem_ipsum, 7, 'Lorem! ipsum...'),
        (lorem_ipsum, 100, 'Lorem! ipsum dolor sit amet, consectetur adipiscing elit. Etiam '
                           'tincidunt consequat lacus vel vestibulum...')
))
def test_word_wrap(text, value, result):
    assert word_wrap(text, value) == result
