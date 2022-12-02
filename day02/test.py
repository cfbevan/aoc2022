from unittest import TestCase
from unittest import main

from .main import calc_round_outcome
from .main import calc_round_score
from .main import calc_your_move
from .main import parse_round_pt1
from .main import parse_round_pt2
from .main import RPS
from .main import Outcome
from .main import pt1
from .main import pt2

input = '\n'.join([
    'A Y',
    'B X',
    'C Z'
])

class Testday02(TestCase):

    def test_parse_round_pt1(self):
        self.assertEqual(parse_round_pt1('A Y'), (RPS.ROCK, RPS.PAPER))
        self.assertEqual(parse_round_pt1('B X'), (RPS.PAPER, RPS.ROCK))
        self.assertEqual(parse_round_pt1('C Z'), (RPS.SCISSORS, RPS.SCISSORS))

    def test_calc_round_outcome(self):
        self.assertEqual(calc_round_outcome(RPS.ROCK, RPS.ROCK), Outcome.TIE)
        self.assertEqual(calc_round_outcome(RPS.ROCK, RPS.PAPER), Outcome.LOSE)
        self.assertEqual(calc_round_outcome(RPS.ROCK, RPS.SCISSORS), Outcome.WIN)
        self.assertEqual(calc_round_outcome(RPS.PAPER, RPS.ROCK), Outcome.WIN)
        self.assertEqual(calc_round_outcome(RPS.PAPER, RPS.PAPER), Outcome.TIE)
        self.assertEqual(calc_round_outcome(RPS.PAPER, RPS.SCISSORS), Outcome.LOSE)
        self.assertEqual(calc_round_outcome(RPS.SCISSORS, RPS.ROCK), Outcome.LOSE)
        self.assertEqual(calc_round_outcome(RPS.SCISSORS, RPS.PAPER), Outcome.WIN)
        self.assertEqual(calc_round_outcome(RPS.SCISSORS, RPS.SCISSORS), Outcome.TIE)

    def test_calc_round_score(self):
        self.assertEqual(calc_round_score(RPS.PAPER, Outcome.WIN), 8)
        self.assertEqual(calc_round_score(RPS.ROCK, Outcome.LOSE), 1)
        self.assertEqual(calc_round_score(RPS.SCISSORS, Outcome.TIE), 6)
        
    def test_calc_your_move(self):
        self.assertEqual(calc_your_move(RPS.ROCK, Outcome.WIN), RPS.PAPER)
        self.assertEqual(calc_your_move(RPS.ROCK, Outcome.LOSE), RPS.SCISSORS)
        self.assertEqual(calc_your_move(RPS.ROCK, Outcome.TIE), RPS.ROCK)
        self.assertEqual(calc_your_move(RPS.PAPER, Outcome.WIN), RPS.SCISSORS)
        self.assertEqual(calc_your_move(RPS.PAPER, Outcome.LOSE), RPS.ROCK)
        self.assertEqual(calc_your_move(RPS.PAPER, Outcome.TIE), RPS.PAPER)
        self.assertEqual(calc_your_move(RPS.SCISSORS, Outcome.WIN), RPS.ROCK)
        self.assertEqual(calc_your_move(RPS.SCISSORS, Outcome.LOSE), RPS.PAPER)
        self.assertEqual(calc_your_move(RPS.SCISSORS, Outcome.TIE), RPS.SCISSORS)

    def test_parse_round_pt2(self):
        self.assertEqual(parse_round_pt2('A Y'), (RPS.ROCK, RPS.ROCK, Outcome.TIE))
        self.assertEqual(parse_round_pt2('B X'), (RPS.PAPER, RPS.ROCK, Outcome.LOSE))
        self.assertEqual(parse_round_pt2('C Z'), (RPS.SCISSORS, RPS.ROCK, Outcome.WIN))

    def test_pt1(self):
        output = pt1(input)
        expected = 15
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 12
        self.assertEqual(output, expected)
        
if __name__ == '__main__':
    main()