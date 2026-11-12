
import pytest
from hypothesis import given, strategies as st
from coupon_validator import split_code, most_expensive, expiry_days


@given(st.one_of(st.text(), st.none()))
def test_split_code_no_crash(s):
    try:
        split_code(s)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_most_expensive_no_crash(s):
    try:
        most_expensive(s)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_expiry_days_no_crash(s):
    try:
        expiry_days(s)
    except ValueError:
        pass
