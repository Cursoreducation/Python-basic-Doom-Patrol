import pytest
import functions_pytest as fp
import functions_for_testing as test_funcs


def test_season():
    assert fp.season('snow') == 'winter'
    assert fp.season('sun') == 'summer'
    assert fp.season('asdasdsa') is None


def test_range_list():
    assert 6 in fp.range_list(5, 10)
    assert 150 in fp.range_list(10, 200)
    assert 1500 in fp.range_list(10, 2000)


def test_div():
    assert test_funcs.div(25, 5) == 5
    assert test_funcs.div(12, 2) == 5
