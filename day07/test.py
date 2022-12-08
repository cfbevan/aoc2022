from unittest import TestCase
from unittest import main

from .main import ComSystem
from .main import pt1
from .main import pt2

input = "\n".join(
    [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]
)


class Testday07(TestCase):
    def test_run(self):
        cs = ComSystem()
        cs.run(input)
        self.assertEqual(
            dict(cs.filesystem),
            {
                "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596},
                "b.txt": 14848514,
                "c.dat": 8504156,
                "d": {"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296},
            },
        )

    def test_get_size(self):
        cs = ComSystem()
        cs.run(input)
        root = cs.filesystem
        self.assertEqual(root.get_child("a").get_child("e").size({}), 584)
        self.assertEqual(root.get_child("a").size({}), 94853)
        self.assertEqual(root.get_child("d").size({}), 24933642)
        self.assertEqual(root.size({}), 48381165)

    def test_get_small_dirs(self):
        cs = ComSystem()
        cs.run(input)
        self.assertEqual(cs.get_small_dirs(100000), [584, 94853])

    def test_pt1(self):
        output = pt1(input)
        expected = 95437
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 24933642
        self.assertEqual(output, expected)


if __name__ == "__main__":
    main()
