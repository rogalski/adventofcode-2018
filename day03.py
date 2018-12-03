import re
import typing
import dataclasses


@dataclasses.dataclass
class Entry:
    label: int
    x: int
    y: int
    w: int
    h: int

    @classmethod
    def from_str(cls, s):
        return cls.from_match(re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", s))

    @classmethod
    def from_match(cls, m):
        label, x, y, w, h = map(int, m.groups())
        return cls(label, x, y, w, h)


def multiple_claims_count(seq: typing.Iterable[str]) -> int:
    items = [Entry.from_str(item) for item in seq]
    W = max(item.x + item.w for item in items)
    H = max(item.y + item.h for item in items)
    arr = [[None for _ in range(W)] for _ in range(H)]
    for item in items:
        for x in range(item.x, item.x + item.w):
            for y in range(item.y, item.y + item.h):
                if arr[x][y] is not None:
                    arr[x][y] = "X"
                else:
                    arr[x][y] = item.label

    return sum(v == "X" for row in arr for v in row)


def only_non_overlapping(seq: typing.Iterable[str]) -> int:
    items = [Entry.from_str(item) for item in seq]
    W = max(item.x + item.w for item in items)
    H = max(item.y + item.h for item in items)
    arr = [[None for _ in range(W)] for _ in range(H)]
    overlapping = set()
    for item in items:
        for x in range(item.x, item.x + item.w):
            for y in range(item.y, item.y + item.h):
                if arr[x][y] is not None:
                    overlapping.add(arr[x][y])
                    overlapping.add(item.label)
                    arr[x][y] = "X"
                else:
                    arr[x][y] = item.label

    return [item.label for item in items if item.label not in overlapping][0]


if __name__ == "__main__":
    with open("day03.txt") as fh:
        print(multiple_claims_count(fh))
    with open("day03.txt") as fh:
        print(only_non_overlapping(fh))
