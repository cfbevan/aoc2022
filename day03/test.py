from unittest import TestCase
from unittest import main

from .main import find_doubled_item
from .main import find_group
from .main import pt1
from .main import pt2

input = "\n".join(
    [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
)


class Testday03(TestCase):
    def test_find_doubled_item(self):
        self.assertEqual(find_doubled_item("vJrwpWtwJgWrhcsFMMfFFhFp"), 16)
        self.assertEqual(find_doubled_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"), 38)
        self.assertEqual(find_doubled_item("PmmdzqPrVvPwwTWBwg"), 42)
        self.assertEqual(find_doubled_item("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"), 22)
        self.assertEqual(find_doubled_item("ttgJtRGJQctTZtZT"), 20)
        self.assertEqual(find_doubled_item("CrZsJsPPZsGzwwsLwLmpwMDw"), 19)

    def test_find_group(self):
        self.assertEqual(
            find_group(
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ),
            18,
        )
        self.assertEqual(
            find_group(
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ),
            52,
        )

    def test_pt1(self):
        output = pt1(input)
        expected = 157
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 70
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
