import string

PRIORITIES = ["", *string.ascii_lowercase, *string.ascii_uppercase]


def find_doubled_item(sack: str) -> int:
    """Find character that is in first and last half of string.

    Return priority value.
    """
    half = int(len(sack) / 2)
    return PRIORITIES.index(set(sack[:half]).intersection(sack[half:]).pop())


def find_group(*groups: list[str]) -> int:
    """Find the badge item of a group.

    Return priority value.
    """
    return PRIORITIES.index(
        set(groups[0]).intersection(*[set(g) for g in groups[1:]]).pop()
    )


def pt1(input: str) -> str:
    return sum([find_doubled_item(sack.strip()) for sack in input.split("\n")])


def pt2(input: str) -> str:
    size = 3
    lines = input.split("\n")
    return sum(
        [
            find_group(g1, g2, g3)
            for g1, g2, g3 in [
                lines[pos : pos + size] for pos in range(0, len(lines), size)
            ]
        ]
    )


if __name__ == "__main__":
    with open("day03/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
