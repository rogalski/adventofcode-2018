import pytest

from day05 import reduce


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ("aA", ""),
        ("abBA", ""),
        ("abAB", "abAB"),
        ("aabAAB", "aabAAB"),
        ("dabAcCaCBAcCcaDA", "dabCBAcaDA"),
    ],
)
def test_reduce(input, expected):
    assert expected == reduce(input)
