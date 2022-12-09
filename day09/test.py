from unittest import TestCase
from unittest import main

from .main import Rope
from .main import Point
from .main import Tail
from .main import pt1
from .main import pt2

input = "\n".join(["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"])

input2 = "\n".join(["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"])


class Testday09(TestCase):
    def test_distance(self):
        self.assertEqual(
            Point(0, 0).distance(Point(0, 0)),
            0,
        )
        self.assertEqual(
            Point(0, 0).distance(Point(1, 0)),
            1,
        )
        self.assertEqual(
            Point(0, 0).distance(Point(0, 1)),
            1,
        )
        self.assertEqual(
            Point(0, 0).distance(Point(1, 1)),
            1,
        )
        self.assertEqual(
            Point(0, 0).distance(Point(1, 2)),
            2,
        )

    def test_tail(self):
        t = Tail(1)
        t.move_to(1, 0)
        self.assertEqual(t, Point(0, 0))
        t.move_to(1, 1)
        self.assertEqual(t, Point(0, 0))
        t.move_to(1, 2)
        self.assertEqual(t, Point(1, 1))

    def test_pt1(self):
        output = pt1(input)
        expected = 13
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input2)
        # expected = 1
        expected = 36
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
