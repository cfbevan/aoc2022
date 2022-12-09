from typing import Type
from math import sqrt, pow, floor


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: Type["Point"]) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def distance(self, pt: Type["Point"]) -> int:
        return floor(sqrt(pow(pt.x - self.x, 2) + pow(pt.y - self.y, 2)))

    def move_to(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, dir: str) -> None:
        match dir:
            case "U":
                self.move_to(self.x, self.y + 1)
            case "D":
                self.move_to(self.x, self.y - 1)
            case "R":
                self.move_to(self.x + 1, self.y)
            case "L":
                self.move_to(self.x - 1, self.y)


class Head(Point):
    ...


class Tail(Point):
    def __init__(self, length: int, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)
        self.length = length
        self.visited: set[tuple[int, int]] = set()

    def __str__(self) -> str:
        return f"({self.x},{self.y})[{str(self.visited)}]"

    def move_to(self, x: int, y: int) -> None:
        if (
            self == Point(x - 1, y + 2)
            or self == Point(x, y + 2)
            or self == Point(x + 1, y + 2)
        ):
            self.x = x
            self.y = y + 1
        elif (
            self == Point(x - 1, y - 2)
            or self == Point(x, y - 2)
            or self == Point(x + 1, y - 2)
        ):
            self.x = x
            self.y = y - 1
        elif (
            self == Point(x - 2, y - 1)
            or self == Point(x - 2, y)
            or self == Point(x - 2, y + 1)
        ):
            self.x = x - 1
            self.y = y
        elif (
            self == Point(x + 2, y - 1)
            or self == Point(x + 2, y)
            or self == Point(x + 2, y + 1)
        ):
            self.x = x + 1
            self.y = y
        elif self == Point(x - 2, y - 2):
            self.x = x - 1
            self.y = y - 1
        elif self == Point(x - 2, y + 2):
            self.x = x - 1
            self.y = y + 1
        elif self == Point(x + 2, y - 2):
            self.x = x + 1
            self.y = y - 1
        elif self == Point(x + 2, y + 2):
            self.x = x + 1
            self.y = y + 1
        self.visited.add((self.x, self.y))


class Rope:
    def __init__(self, knots, x: int = 0, y: int = 0) -> None:
        self.start = Point(x, y)
        self.knots = [Head(x, y)]
        for _ in range(1, knots):
            self.knots.append(Tail(x, y))

    def move(self, dir: str, times: int, debug: int = 0) -> None:
        for _ in range(0, times):
            self.knots[0].move(dir)
            for i, k in enumerate(self.knots[1:]):
                previous_knot = self.knots[i]
                k.move_to(previous_knot.x, previous_knot.y)
            if debug > 1:
                print(str(self), "\n")
        if debug > 1:
            print("\n")

    def run(self, input: str, debug: int = 0) -> None:
        if debug > 0:
            print("== Initial State ==\n\n")
            print(str(self), "\n\n")
        for row in input.split("\n"):
            (d, t) = row.strip().split()
            if debug > 0:
                print(f"== {row} ==\n\n")
            self.move(d, int(t, 10), debug)
            if debug == 1:
                print(str(self), "\n\n")

    def __str__(self) -> str:
        return ", ".join([f"({k.x}, {k.y})" for k in self.knots])


def pt1(input: str) -> int:
    r = Rope(2)
    r.run(input)
    return len(r.knots[-1].visited)


def pt2(input: str) -> str:
    r = Rope(10)
    r.run(input, debug=0)
    return len(r.knots[-1].visited)


if __name__ == "__main__":
    with open("day09/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
