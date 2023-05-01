import fuel
import pytest

def main():
    test_convert()
    test_gauge()
    test_gauge_emptiness()
    test_gauge_fullness()
    test_raises_zeroDivisionError()
    test_raises_irregularNumberError()
    test_raises_noNumberError()


def test_convert():
    assert fuel.convert("1/5") == 20
    # assert fuel.convert("1/7") == 14
    # assert fuel.convert("1/8") == 13
    # assert fuel.convert("1/9") == 11
    # assert fuel.convert("2/23") == 9


def test_gauge_emptiness():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"

def test_gauge_fullness():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"

def test_gauge():
    assert fuel.gauge(65) == "65%"

def test_raises_zeroDivisionError():
    with pytest.raises(Exception):
        fuel.convert("2/0")

def test_raises_irregularNumberError():
    with pytest.raises(Exception):
        fuel.convert("3/1")

def test_raises_noNumberError():
    with pytest.raises(Exception):
        fuel.convert("3/k")

if __name__ == "__main__":
    main()