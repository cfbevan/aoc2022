from enum import Enum
from typing import Literal


class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Outcome(Enum):
    WIN = 0
    LOSE = 1
    TIE = 2


score_shape: dict[RPS, int] = {RPS.ROCK: 1, RPS.PAPER: 2, RPS.SCISSORS: 3}

score_outcome: dict[Outcome, int] = {Outcome.WIN: 6, Outcome.LOSE: 0, Outcome.TIE: 3}

decode_you: dict[Literal["X", "Y", "Z"], RPS] = {
    "X": RPS.ROCK,
    "Y": RPS.PAPER,
    "Z": RPS.SCISSORS,
}

decode_outcome: dict[Literal["X", "Y", "Z"], Outcome] = {
    "X": Outcome.LOSE,
    "Y": Outcome.TIE,
    "Z": Outcome.WIN,
}

decode_them: dict[Literal["A", "B", "C"], RPS] = {
    "A": RPS.ROCK,
    "B": RPS.PAPER,
    "C": RPS.SCISSORS,
}


def calc_round_outcome(you: RPS, them: RPS) -> Outcome:
    if you == them:
        return Outcome.TIE
    elif you == RPS.ROCK:
        if them == RPS.PAPER:
            return Outcome.LOSE
        return Outcome.WIN
    elif you == RPS.PAPER:
        if them == RPS.SCISSORS:
            return Outcome.LOSE
        return Outcome.WIN
    elif you == RPS.SCISSORS:
        if them == RPS.ROCK:
            return Outcome.LOSE
        return Outcome.WIN


def calc_your_move(them: RPS, outcome: Outcome) -> RPS:
    if outcome == Outcome.TIE:
        return them
    elif outcome == Outcome.LOSE:
        if them == RPS.ROCK:
            return RPS.SCISSORS
        elif them == RPS.PAPER:
            return RPS.ROCK
        return RPS.PAPER
    elif outcome == Outcome.WIN:
        if them == RPS.ROCK:
            return RPS.PAPER
        elif them == RPS.PAPER:
            return RPS.SCISSORS
        return RPS.ROCK


def calc_round_score(you: RPS, outcome: Outcome) -> int:
    return score_shape[you] + score_outcome[outcome]


def parse_round_pt1(round: str) -> tuple[RPS, RPS]:
    t, y = round.strip().split(" ")
    return (decode_them[t.strip()], decode_you[y.strip()])


def parse_round_pt2(round: str) -> tuple[RPS, RPS, Outcome]:
    t, o = round.strip().split(" ")
    them = decode_them[t.strip()]
    outcome = decode_outcome[o.strip()]
    return (them, calc_your_move(them, outcome), outcome)


def pt1(input: str) -> str:
    score = 0
    for row in input.split("\n"):
        (them, you) = parse_round_pt1(row)
        score += calc_round_score(you, calc_round_outcome(you, them))
    return score


def pt2(input: str) -> str:
    score = 0
    for row in input.split("\n"):
        (_, you, outcome) = parse_round_pt2(row)
        score += calc_round_score(you, outcome)
    return score


if __name__ == "__main__":
    with open("day02/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
