from unittest import TestCase
from unittest import main

from .main import Scan
from .main import pt1
from .main import pt2

input = ""
with open("day14/test_input.txt", "r") as fin:
    input = fin.read().strip()


class Testday14(TestCase):
    def test_init_scan(self):
        s = Scan(input)
        self.assertEqual(
            str(s),
            (
                "......+...\n"
                "..........\n"
                "..........\n"
                "..........\n"
                "....#...##\n"
                "....#...#.\n"
                "..###...#.\n"
                "........#.\n"
                "........#.\n"
                "#########."
            ),
        )

    def test_pt1(self):
        output = pt1(input)
        expected = 24
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 93
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
