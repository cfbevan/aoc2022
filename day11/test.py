from unittest import TestCase
from unittest import main

from .main import Monkey, MitM
from .main import pt1
from .main import pt2

input = ""
with open("day11/test_input.txt") as fin:
    input = fin.read()


class Testday11(TestCase):
    def test_create_monkey(self):
        input = """Monkey 0:
        Starting items: 79, 98
        Operation: new = old * 19
        Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
        """
        m = Monkey(input)
        self.assertEqual(m.id, 0)
        self.assertEqual(m.items, [79, 98])
        self.assertEqual(m.operation(1), 19)
        self.assertEqual(m.test, 23)
        self.assertEqual(m.test_true, 2)
        self.assertEqual(m.test_false, 3)
        self.assertEqual(m.inspections, 0)

    def test_create_monkey2(self):
        input = """Monkey 2:
        Starting items: 79, 60, 97
        Operation: new = old * old
        Test: divisible by 13
            If true: throw to monkey 1
            If false: throw to monkey 3
        """
        m = Monkey(input)
        self.assertEqual(m.id, 2)
        self.assertEqual(m.items, [79, 60, 97])
        self.assertEqual(m.operation(1), 1)
        self.assertEqual(m.test, 13)
        self.assertEqual(m.test_true, 1)
        self.assertEqual(m.test_false, 3)
        self.assertEqual(m.inspections, 0)

    def test_pt1(self):
        output = pt1(input)
        expected = "10605"
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = "2713310158"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
