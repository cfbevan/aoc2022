class Forest:
    def __init__(self, map: str) -> None:
        self.map = self._parse_map(map)

    def _parse_map(self, data: str) -> list[list[int]]:
        map = []
        for row in data.split("\n"):
            map.append([int(c, 10) for c in row.strip()])
        return map

    @property
    def rows(self):
        return len(self.map)

    @property
    def cols(self):
        return len(self.map[0])

    def is_edge(self, row: int, col: int) -> bool:
        return row == 0 or row == (self.rows - 1) or col == 0 or col == (self.cols - 1)

    def is_visible(self, row: int, col: int) -> bool:
        if self.is_edge(row, col):
            return True
        value = self.map[row][col]
        _row = self.map[row]
        _column = [r[col] for r in self.map]
        return (
            max(_row[:col]) < value
            or max(_row[col + 1 :]) < value
            or max(_column[:row]) < value
            or max(_column[row + 1 :]) < value
        )

    def score(self, row: int, col: int) -> int:
        value = self.map[row][col]
        _row = self.map[row]
        _column = [r[col] for r in self.map]
        # up
        up = 0
        for x in reversed(_column[:row]):
            up += 1
            if x >= value:
                break
        # down
        down = 0
        for x in _column[row + 1 :]:
            down += 1
            if x >= value:
                break
        # left
        left = 0
        for x in reversed(_row[:col]):
            left += 1
            if x >= value:
                break
        # right
        right = 0
        for x in _row[col + 1 :]:
            right += 1
            if x >= value:
                break
        return up * down * left * right

    def get_visible(self) -> list[list[bool]]:
        map = []
        for r in range(0, self.rows):
            map.append([self.is_visible(r, c) for c in range(0, self.cols)])
        return map

    def get_score(self) -> list[list[int]]:
        map = []
        for r in range(0, self.rows):
            map.append([self.score(r, c) for c in range(0, self.cols)])
        return map

    def count_visible(self) -> int:
        return sum([sum([int(c) for c in r]) for r in self.get_visible()])

    def highest_senic_score(self) -> int:
        return max([max(r) for r in self.get_score()])

    def print_size(self) -> str:
        return "\n".join(["".join([str(c) for c in r]) for r in self.map])

    def print_score(self) -> str:
        return "\n".join([",".join([str(c) for c in r]) for r in self.get_score()])

    def print_visible(self) -> str:
        return "\n".join(
            ["".join(["T" if c else "F" for c in r]) for r in self.get_visible()]
        )


def pt1(input: str) -> int:
    f = Forest(input)
    return f.count_visible()


def pt2(input: str) -> int:
    f = Forest(input)
    return f.highest_senic_score()


if __name__ == "__main__":
    with open("day08/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
