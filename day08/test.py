from unittest import TestCase
from unittest import main

from .main import Forest
from .main import pt1
from .main import pt2

input = "\n".join(["30373", "25512", "65332", "33549", "35390"])


class Testday08(TestCase):
    def test_parse(self):
        f = Forest(input)
        self.assertEqual(
            f.print_size(), "\n".join(["30373", "25512", "65332", "33549", "35390"])
        )

    def test_is_edge(self):
        f = Forest(input)
        self.assertEqual(f.is_edge(0, 1), True)
        self.assertEqual(f.is_edge(4, 1), True)
        self.assertEqual(f.is_edge(1, 0), True)
        self.assertEqual(f.is_edge(1, 4), True)
        self.assertEqual(f.is_edge(1, 1), False)
        self.assertEqual(f.is_edge(2, 2), False)

    def test_is_visible(self):
        f = Forest(input)
        self.assertEqual(f.is_visible(0, 1), True)
        self.assertEqual(f.is_visible(4, 1), True)
        self.assertEqual(f.is_visible(1, 0), True)
        self.assertEqual(f.is_visible(1, 4), True)
        self.assertEqual(f.is_visible(1, 1), True)
        self.assertEqual(f.is_visible(1, 2), True)
        self.assertEqual(f.is_visible(1, 3), False)
        self.assertEqual(f.is_visible(2, 1), True)
        self.assertEqual(f.is_visible(2, 2), False)
        self.assertEqual(f.is_visible(2, 3), True)
        self.assertEqual(f.is_visible(3, 1), False)
        self.assertEqual(f.is_visible(3, 2), True)
        self.assertEqual(f.is_visible(3, 3), False)

    def test_print_visible(self):
        f = Forest(input)
        self.assertEqual(
            f.print_visible(), "\n".join(["TTTTT", "TTTFT", "TTFTT", "TFTFT", "TTTTT"])
        )

    def test_score(self):
        f = Forest(input)
        self.assertEqual(f.score(0, 0), 0)
        self.assertEqual(f.score(1, 2), 4)
        self.assertEqual(f.score(3, 2), 8)

    def test_print_score(self):
        f = Forest(input)
        self.assertEqual(
            f.print_score(),
            "\n".join(
                ["0,0,0,0,0", "0,1,4,1,0", "0,6,1,2,0", "0,1,8,3,0", "0,0,0,0,0"]
            ),
        )

    def test_pt1(self):
        output = pt1(input)
        expected = 21
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 8
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
