from re import findall, match
from typing import Any
from io import StringIO
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(message)s", level=logging.ERROR)


class Stacks:
    def __init__(self, diagram: str) -> None:
        self._stacks = defaultdict(list)
        self._parse_diagram(diagram)

    @property
    def stacks(self) -> dict[str, Any]:
        return dict(self._stacks)

    @property
    def tops(self) -> str:
        """Return the top crate of each stack."""
        output = []
        for key in sorted(self.stacks.keys()):
            output.append(self.stacks[key][-1])
        return "".join(output)

    def _parse_diagram(self, diagram: str):
        """Parse a diagram into stacks.

        Args:
            diagram (str): String representation of diagram.
        """
        for row in diagram.split("\n"):
            matches = findall(r"(   |\[[A-Z]\])\s?", row)
            index = 1
            for match in matches:
                if match[1] != " ":
                    self._stacks[index].append(match[1])
                index += 1
        for k, v in self._stacks.items():
            self._stacks[k] = list(reversed(v))

    def _move(self, count: int, start: int, end: int):
        """9000 version of move."""
        for _ in range(0, count):
            self._stacks[end].append(self._stacks[start].pop())

    def _move2(self, count: int, start: int, end: int):
        """9001 version of move."""
        crane = []
        for _ in range(0, count):
            crane.append(self._stacks[start].pop())
        for _ in range(0, count):
            self._stacks[end].append(crane.pop())

    def move(self, input: str, new_version: bool = False):
        """Perform a move action.

        Args:
            input (str): Move description
        """
        nums = match(r"move (\d+) from (\d+) to (\d+)", input)
        if nums is None:
            return
        groups = nums.groups()
        if new_version:
            self._move2(
                int(groups[0]),
                int(groups[1]),
                int(groups[2]),
            )
        else:
            self._move(
                int(groups[0]),
                int(groups[1]),
                int(groups[2]),
            )

    def __str__(self) -> str:
        """Print the stack as a diagram."""
        out = StringIO()
        size = max([len(self.stacks[key]) for key in self.stacks.keys()])
        for index in range(size, -1, -1):
            for key in sorted(self.stacks.keys()):
                if index < len(self.stacks[key]):
                    c = self.stacks[key][index]
                    out.write(f"[{c}] ")
                else:
                    out.write("    ")
            out.write("\n")
        for index in range(1, len(self.stacks.keys()) + 1):
            out.write(f" {index}  ")
        out.flush()
        v = out.getvalue()
        out.close()
        return v


def pt1(input: str) -> str:
    (diagram, moves) = input.split("\n\n")
    s = Stacks(diagram)
    for move in moves.split("\n"):
        logger.debug("=" * 50)
        logger.debug(str(s))
        logger.debug("-" * 50)
        logger.debug(move)
        s.move(move.strip())
        logger.debug("-" * 50)
        logger.debug(str(s))
        logger.debug("=" * 50)
    return s.tops


def pt2(input: str) -> str:
    (diagram, moves) = input.split("\n\n")
    s = Stacks(diagram)
    for move in moves.split("\n"):
        logger.debug("=" * 50)
        logger.debug(str(s))
        logger.debug("-" * 50)
        logger.debug(move)
        s.move(move.strip(), True)
        logger.debug("-" * 50)
        logger.debug(str(s))
        logger.debug("=" * 50)
    return s.tops


if __name__ == "__main__":
    with open("day05/input.txt", "r") as fin:
        input = fin.read()
        print(pt1(input))
        print(pt2(input))
