import pytest
from coupon_validator import coupon_discount, best_discount, is_expired


def test_empty_cart():
    with pytest.raises(ValueError):
        coupon_discount("WELCOME10", 0, True, "mon")


def test_welcome_branches():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0


def test_weekend_branches():
    assert coupon_discount("WEEKEND20", 600, False, "sat") == 120
    assert coupon_discount("WEEKEND20", 200, False, "sun") == 50
    assert coupon_discount("WEEKEND20", 600, False, "mon") == 0


def test_flat_branches():
    assert coupon_discount("FLAT100", 400, False, "mon") == 100
    assert coupon_discount("FLAT100", 300, False, "mon") == 0


def test_invalid_coupon():
    assert coupon_discount("INVALID", 500, True, "sat") == 0


def test_best_discount_branches():
    assert best_discount([], 200, False, "mon") == 0
    assert best_discount(["WELCOME10"], 200, True, "mon") == 20
    assert best_discount(["WELCOME10", "INVALID"], 200, True, "mon") == 20
    assert best_discount(["WEEKEND20"], 100, False, "sat") == 40
    assert best_discount(["FLAT100"], 400, False, "mon") == 100


def test_expiry_branches():
    assert is_expired(10, 5, 0) is True
    assert is_expired(20, 5, 10) is True
    assert is_expired(10, 5, 10) is False
