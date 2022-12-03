import string

PRIORITIES = ["", *string.ascii_lowercase, *string.ascii_uppercase]


def find_doubled_item(sack: str) -> tuple[str, int]:
    """Find character that is in first and last half of string.

    Return character and priority value.
    """
    half = int(len(sack) / 2)
    letter = set(sack[:half]).intersection(sack[half:]).pop()
    return letter, PRIORITIES.index(letter)


def find_group(*groups: list[str]) -> tuple[str, int]:
    """Find the badge item of a group.

    Return item and priority value.
    """
    letter = set(groups[0]).intersection(*[set(g) for g in groups[1:]]).pop()
    return letter, PRIORITIES.index(letter)


def pt1(input: str) -> str:
    sum = 0
    for sack in input.split("\n"):
        sum += find_doubled_item(sack.strip())[1]
    return sum


def pt2(input: str) -> str:
    sum = 0
    lines = input.split("\n")
    for g1, g2, g3 in [lines[pos : pos + 3] for pos in range(0, len(lines), 3)]:
        sum += find_group(g1, g2, g3)[1]
    return sum


if __name__ == "__main__":
    with open("day03/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
