import pytest

from day01 import final_freq, first_reached_twice


@pytest.mark.parametrize(
    ["input", "expected"],
    [("+1 -2 +3 +1", 3), ("+1 +1 +1", 3), ("+1 +1 -2", 0), ("-1 -2 -3", -6)],
)
def test_final_freq(input, expected):
    assert expected == final_freq(input)


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ("+1 -1", 0),
        ("+3 +3 +4 -2 -4", 10),
        ("-6 +3 +8 +5 -6", 5),
        ("+7 +7 -2 -7 -4", 14),
    ],
)
def test_first_reached_twice(input, expected):
    assert expected == first_reached_twice(input)
