import string


def reduce(s: str) -> str:
    while True:
        reduced = reduce_once(s)
        if reduced == s:
            return reduced
        s = reduced


def reduce_once(s: str) -> str:
    codes = list(map(ord, s))
    deltas = [abs(c1 - c0) for c0, c1 in zip(codes, codes[1:])]
    pairs_to_delete = [(idx, idx + 1) for idx, d in enumerate(deltas) if d == 32]
    # this can likely be optimized
    for p1, p2 in list(zip(pairs_to_delete, pairs_to_delete[1:])):
        if p1[1] == p2[0]:
            pairs_to_delete.remove(p2)
    indicies_to_delete = [idx for pair in pairs_to_delete for idx in pair]
    return "".join(c for idx, c in enumerate(s) if idx not in indicies_to_delete)


if __name__ == "__main__":
    with open("day05.txt") as fh:
        data = fh.read()

    print(len(reduce(data)))
    for c in string.ascii_lowercase:
        data_c = data.replace(c, "").replace(c.upper(), "")
        print(c, len(reduce(data_c)))
