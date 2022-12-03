def calc_cals(input: str) -> list[int]:
    """Calculate sorted calories. Lowest to highest."""
    elves = []
    elf = []
    for row in input.split("\n"):
        cal = row.strip()
        if cal == "":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(cal, 10))
    elves.append(elf)
    return sorted([sum(elf) for elf in elves])


def pt1(input: str) -> str:
    return calc_cals(input)[-1]


def pt2(input: str) -> str:
    cals = calc_cals(input)
    return cals[-1] + cals[-2] + cals[-3]


if __name__ == "__main__":
    with open("day01/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
