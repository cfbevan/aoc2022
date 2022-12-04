
def parse_range(str_range: str) -> set[int]:
    """Parse a range to a set of ints.

    Args:
        range (str): String range of form \d+-\d+.

    Returns:
        set[int]: Set representing the range.
    """
    (_from, to) = str_range.split('-')
    return set(range(int(_from, 10), int(to, 10) + 1))

def fully_contain(area1: set, area2: set) -> bool:
    """Check if any single area fully contains another.

    Returns:
        bool: True if any area fully contains the other.
    """
    return area1.issuperset(area2) or area2.issuperset(area1)

def overlap(area1: set, area2: set) -> bool:
    """Get the number of items that are in each set.

    Returns:
        int: Number of overlapping items
    """
    return len(area1.intersection(area2)) > 0

def pt1(input: str) -> int:
    count = 0
    for row in input.split('\n'):
        (r1, r2) = row.strip().split(',')
        if fully_contain(parse_range(r1), parse_range(r2)):
            count += 1
    return count

def pt2(input: str) -> str:
    count = 0
    for row in input.split('\n'):
        (r1, r2) = row.strip().split(',')
        if overlap(parse_range(r1), parse_range(r2)):
            count += 1
    return count

if __name__ == '__main__':
    with open('day04/input.txt', 'r') as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
