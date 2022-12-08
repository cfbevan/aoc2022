from unittest import TestCase
from unittest import main

from .main import parse_range
from .main import fully_contain
from .main import overlap
from .main import pt1
from .main import pt2

input = "\n".join(
    [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]
)


class Testday04(TestCase):
    def test_parse_range(self):
        self.assertEqual(parse_range("2-4"), {2, 3, 4})
        self.assertEqual(parse_range("1-2"), {1, 2})
        self.assertEqual(parse_range("6-6"), {6})
        self.assertEqual(parse_range("100-101"), {100, 101})

    def test_fully_contain(self):
        self.assertEqual(fully_contain({2, 3, 4}, {6, 7, 8}), False)
        self.assertEqual(fully_contain({6, 7, 8}, {2, 3, 4}), False)
        self.assertEqual(fully_contain({6}, {6}), True)
        self.assertEqual(fully_contain({6}, {4, 5, 6}), True)
        self.assertEqual(fully_contain({4, 5, 6}, {6}), True)
        self.assertEqual(fully_contain({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}), True)

    def test_calc_overlap(self):
        self.assertEqual(overlap({2, 3, 4}, {6, 7, 8}), False)
        self.assertEqual(overlap({5, 6, 7}, {7, 8, 9}), True)

    def test_pt1(self):
        output = pt1(input)
        expected = 2
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 4
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
