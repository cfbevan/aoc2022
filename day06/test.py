from unittest import TestCase
from unittest import main

from .main import ComDevice
from .main import pt1
from .main import pt2

input = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    "aaaaabcd",
]


class Testday06(TestCase):
    def test_find_packet(self):
        cd = ComDevice()
        cd.stream = input[0]
        self.assertEqual(cd.find_start_of_packet(), 7)
        cd.stream = input[1]
        self.assertEqual(cd.find_start_of_packet(), 5)
        cd.stream = input[2]
        self.assertEqual(cd.find_start_of_packet(), 6)
        cd.stream = input[3]
        self.assertEqual(cd.find_start_of_packet(), 10)
        cd.stream = input[4]
        self.assertEqual(cd.find_start_of_packet(), 11)
        cd.stream = input[5]
        self.assertEqual(cd.find_start_of_packet(), 8)

    def test_find_message(self):
        cd = ComDevice()
        cd.window = 14
        cd.stream = input[0]
        self.assertEqual(cd.find_start_of_packet(), 19)
        cd.stream = input[1]
        self.assertEqual(cd.find_start_of_packet(), 23)
        cd.stream = input[2]
        self.assertEqual(cd.find_start_of_packet(), 23)
        cd.stream = input[3]
        self.assertEqual(cd.find_start_of_packet(), 29)
        cd.stream = input[4]
        self.assertEqual(cd.find_start_of_packet(), 26)


if __name__ == "__main__":
    main()
