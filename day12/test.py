from unittest import TestCase
from unittest import main

from .main import HeightMap
from .main import pt1
from .main import pt2

input = "\n".join(["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"])


class Testday12(TestCase):
    def test_get_moves(self):
        hm = HeightMap(input)
        self.assertEqual(hm.get_moves((0, 0)), [(1, 0), (0, 1)])
        self.assertEqual(hm.get_moves((1, 0)), [(0, 0), (2, 0), (1, 1)])
        self.assertEqual(hm.get_moves((2, 4)), [(1, 4), (3, 4), (2, 3), (2, 5)])

    def test_distance_map(self):
        hm = HeightMap(input)
        self.assertEqual(hm.distance_map[(0, 0)], 0)
        self.assertEqual(hm.distance_map[(2, 5)], 31)

    def test_pt1(self):
        output = pt1(input)
        expected = 31
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 29
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main(verbosity=2)
