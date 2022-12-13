from unittest import TestCase
from unittest import main

from .main import Signal, Signal2, Pair
from .main import pt1
from .main import pt2

input = ""
with open("day13/test_input.txt", "r") as fin:
    input = fin.read()


class Testday13(TestCase):
    def test_pair_compare(self):
        self.assertEqual(Pair("[1,1,3,1,1]", "[1,1,5,1,1]").is_in_order(), True)
        self.assertEqual(Pair("[[1],[2,3,4]]", "[[1],4]").is_in_order(), True)
        self.assertEqual(Pair("[9]", "[[8,7,6]]").is_in_order(), False)
        self.assertEqual(Pair("[[4,4],4,4]", "[[4,4],4,4,4]").is_in_order(), True)
        self.assertEqual(Pair("[7,7,7,7]", "[7,7,7]").is_in_order(), False)
        self.assertEqual(Pair("[]", "[3]").is_in_order(), True)
        self.assertEqual(Pair("[[[]]]", "[[]]").is_in_order(), False)
        self.assertEqual(
            Pair(
                "[1,[2,[3,[4,[5,6,7]]]],8,9]", "[1,[2,[3,[4,[5,6,0]]]],8,9]"
            ).is_in_order(),
            False,
        )

    def test_signal(self):
        s = Signal(input)
        self.assertEqual(
            s.correct_order(), [True, True, False, True, False, True, False, False]
        )
        self.assertEqual(s.correct_order_index(), [1, 2, 4, 6])
        self.assertEqual(s.correct_order_sum(), 13)

    def test_signal2(self):
        s = Signal2(input)
        self.assertEqual(
            s.sorted_packets(),
            [
                [],
                [[]],
                [[[]]],
                [1, 1, 3, 1, 1],
                [1, 1, 5, 1, 1],
                [[1], [2, 3, 4]],
                [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
                [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                [[1], 4],
                [[2]],
                [3],
                [[4, 4], 4, 4],
                [[4, 4], 4, 4, 4],
                [[6]],
                [7, 7, 7],
                [7, 7, 7, 7],
                [[8, 7, 6]],
                [9],
            ],
        )
        self.assertEqual(s.divider_packets(), [10, 14])
        self.assertEqual(s.decoder_key(), 140)

    def test_pt1(self):
        output = pt1(input)
        expected = 13
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 140
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
