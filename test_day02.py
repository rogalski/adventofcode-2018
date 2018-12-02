import pytest

from day02 import checksum, common_letters


def test_checksum():
    with open("test_day02.txt") as fh:
        assert 12 == checksum(fh)


def test_common_letters():
    with open("test_day02_part2.txt") as fh:
        assert "fgij" == common_letters(fh)
