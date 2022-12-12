from string import ascii_lowercase


class HeightMap:
    def __init__(self, data: str, include_a_starts: bool = False) -> None:
        self.height_map: list[list[int]] = []
        self.distance_map: dict = {}
        # parse map data
        for (r, row) in enumerate(data.split("\n")):
            r_map = []
            for (c, char) in enumerate(row):
                match char:
                    case "S":
                        self.start = (r, c)
                        r_map.append(ascii_lowercase.index("a"))
                    case "E":
                        self.end = (r, c)
                        r_map.append(ascii_lowercase.index("z"))
                    case _:
                        r_map.append(ascii_lowercase.index(char))
            self.height_map.append(r_map)
        self.make_distance_map(include_a_starts)

    def get_moves(self, node: tuple[int, int]) -> list[tuple[int, int]]:
        """Given a row and col to check, return all possible moves from that point.

        A move can be up, down, left, or right provided the node you are going to is
        at most one level higher than your current node.

        Args:
            r (int): _description_
            c (int): _description_

        Returns:
            list[tuple[int,int]]: List of possible moves
        """
        moves = []
        (r, c) = node
        max_up = self.height_map[r][c] + 1
        # test up
        if r != 0 and self.height_map[r - 1][c] <= max_up:
            moves.append((r - 1, c))
        # test down
        if r != len(self.height_map) - 1 and self.height_map[r + 1][c] <= max_up:
            moves.append((r + 1, c))
        # test left
        if c != 0 and self.height_map[r][c - 1] <= max_up:
            moves.append((r, c - 1))
        # test right
        if c != len(self.height_map[r]) - 1 and self.height_map[r][c + 1] <= max_up:
            moves.append((r, c + 1))
        return moves

    def make_distance_map(
        self,
        include_a_starts: bool,
        node: tuple[int, int] | None = None,
        distance: int | None = None,
    ) -> None:
        if node is None:
            node = self.start
            distance = 0
        if include_a_starts and self.height_map[node[0]][node[1]] == 0:
            distance = 0
        # recursion end cases
        if node[0] == self.end[0] and node[1] == self.end[1]:
            # we found the end, return paths
            self.distance_map[node] = distance
            return None
        if node in self.distance_map and distance >= self.distance_map[node]:
            # we found a path to the same node that is longer than one we already had
            return None
        # record distance to this node and check all paths from this node
        self.distance_map[node] = distance
        for move in self.get_moves(node):
            self.make_distance_map(include_a_starts, move, distance + 1)


def pt1(input: str) -> int:
    hm = HeightMap(input)
    return hm.distance_map[hm.end]


def pt2(input: str) -> str:
    hm = HeightMap(input, True)
    return hm.distance_map[hm.end]


if __name__ == "__main__":
    with open("day12/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
