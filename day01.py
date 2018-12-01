import typing
import itertools


def final_freq(s: str) -> int:
    return sum([int(digit) for digit in s.split()])


def first_reached_twice(s: str) -> int:
    accum = 0
    encountered = {0}
    digits = itertools.cycle(map(int, s.split()))
    for digit in digits:
        accum += digit
        if accum in encountered:
            return accum
        encountered.add(accum)
    raise Exception


if __name__ == "__main__":
    with open("day01.txt") as fh:
        data = fh.read()
        print(final_freq(data))
        print(first_reached_twice(data))
