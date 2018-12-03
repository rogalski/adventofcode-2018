import pytest

from day03 import multiple_claims_count, only_non_overlapping


def test_multiple_claims_count():
    with open("test_day03.txt") as fh:
        assert 4 == multiple_claims_count(fh)


def test_multiple_claims_count():
    with open("test_day03.txt") as fh:
        assert 3 == only_non_overlapping(fh)
