from unittest import TestCase
from unittest import main

from .main import calc_cals
from .main import pt1
from .main import pt2

input = "\n".join(
    [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
)


class Testday01(TestCase):
    def test_calc_cals(self):
        output = calc_cals(input)
        expected = [4000, 6000, 10000, 11000, 24000]
        self.assertEqual(output, expected)

    def test_pt1(self):
        output = pt1(input)
        expected = 24000
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 45000
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
