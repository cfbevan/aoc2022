from __future__ import annotations


class Pt:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __add__(self, __o: Pt) -> Pt:
        return Pt(self.x + __o.x, self.y + __o.y)

    def __sub__(self, __o: Pt) -> Pt:
        return Pt(self.x - __o.x, self.y - __o.y)

    def __eq__(self, __o: Pt) -> bool:
        return self.x == __o.x and self.y == __o.y


class Scan:
    def __init__(self, data: str, start: Pt = Pt(500, 0), floor: bool = False) -> None:
        self.origin = start
        self.map = {str(start): "+"}
        # min/max for size of map
        self.x = (start.x, start.x + 1)
        self.y = (0, 1)
        # grains of sand on screen
        self.sand = 0
        # do we have a floor? (pt2)
        self.floor = floor
        self._parse(data)

    def _parse(self, data: str) -> None:
        for line in data.split("\n"):
            points = [
                (int(x), int(y))
                for x, y in (point.split(",") for point in line.split(" -> "))
            ]
            for (x1, y1), (x2, y2) in zip(points, points[1:]):
                # draw walls in map
                self.map.update(
                    {str(Pt(x, y1)): "#" for x in range(min(x1, x2), max(x1, x2) + 1)}
                )
                self.map.update(
                    {str(Pt(x1, y)): "#" for y in range(min(y1, y2), max(y1, y2) + 1)}
                )
            for x, y in points:
                # update map size
                self.x = (min(self.x[0], x), max(self.x[1], x + 1))
                self.y = (min(self.y[0], x), max(self.y[1], y + 1))
        if self.floor:
            # add one row for floor
            self.y = (self.y[0], self.y[1] + 1)

    def __str__(self) -> str:
        return "\n".join(
            "".join(
                self.map.get(str(Pt(x, y)), ".") for x in range(self.x[0], self.x[1])
            )
            for y in range(self.y[0], self.y[1])
        )

    def drop_sand(self) -> None:
        pos: Pt = Pt(0, 0)
        # drop sand till origin is covered
        while pos != self.origin:
            # start with dropping one straight down
            pos = Pt(self.origin.x, self.origin.y)
            # while y position is on map
            while self.y[0] <= pos.y < self.y[1]:
                # test each possible drop positions
                # down one, left one, right one
                for move in (Pt(0, 1), Pt(-1, 1), Pt(1, 1)):
                    # if on map still, continue
                    if str(pos + move) in self.map:
                        continue
                    # set position to next move
                    pos += move
                    # break to while loop to test next position
                    break
                else:
                    break
            # pos is now final resting place of falling sand
            # if we have floor or pos.y is still on map (not fell off screen)
            if self.floor or self.y[0] <= pos.y < self.y[1]:
                # add to sand count if on screen (retest in case floor was true)
                self.sand += pos.y < self.y[1]
                # set map to sand icon
                self.map[str(pos)] = "o"
                # update screen size if needed
                self.x = (min(self.x[0], int(pos.x)), max(self.x[1], int(pos.x) + 1))
            else:
                # exit while loop, sand fell off screen
                break


def pt1(input: str) -> int:
    s = Scan(input)
    # print(str(s))
    s.drop_sand()
    # print(str(s))
    return s.sand


def pt2(input: str) -> str:
    s = Scan(input, floor=True)
    # print(str(s))
    s.drop_sand()
    # print(str(s))
    return s.sand


if __name__ == "__main__":
    with open("day14/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
