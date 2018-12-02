import typing
import collections


def checksum(seq: typing.Iterable[str]) -> int:
    two_repeated = 0
    three_repeated = 0
    for item in seq:
        item = item.strip()
        counter = collections.Counter(item)
        if any(v == 3 for v in counter.values()):
            three_repeated += 1
        if any(v == 2 for v in counter.values()):
            two_repeated += 1
    return two_repeated * three_repeated


def common_letters(seq: typing.Iterable[str]) -> str:
    # this is n^2 * m, where n is number of items
    # in sequence and m is item length
    # quite inefficient, maybe there is better algorithm somewhere
    seq = [item.strip() for item in seq]
    seq_length = len(seq)
    for idx in range(seq_length):
        str1 = seq[idx]
        for idx2 in range(idx + 1, seq_length):
            str2 = seq[idx2]
            hamming = sum(c1 != c2 for c1, c2 in zip(str1, str2))
            if hamming == 1:
                return "".join(c1 for c1, c2 in zip(str1, str2) if c1 == c2)
    raise ValueError


if __name__ == "__main__":
    with open("day02.txt") as fh:
        print(checksum(fh))
    with open("day02.txt") as fh:
        print(common_letters(fh))
