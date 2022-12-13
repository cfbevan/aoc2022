from __future__ import annotations
from logging import getLogger, basicConfig
from functools import reduce

logger = getLogger(__name__)
basicConfig(level="ERROR")


def is_in_order(left: list, right: list, tab_count: int = 0) -> bool:
    logger.debug("%scompare => %s vs %s", "\t" * tab_count, str(left), str(right))
    for i in range(min(len(left), len(right))):
        logger.debug(
            "%scompare => %s vs %s", "\t" * (tab_count + 1), str(left[i]), str(right[i])
        )
        resp = None
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                logger.debug(
                    "%sleft is smaller, in right order -> True", "\t" * (tab_count + 1)
                )
                return True
            elif left[i] > right[i]:
                logger.debug(
                    "%sright is smaller, out of order -> False", "\t" * (tab_count + 1)
                )
                return False
        elif isinstance(left[i], list) and isinstance(right[i], list):
            resp = is_in_order(left[i], right[i], tab_count + 1)
        elif isinstance(left[i], int) and isinstance(right[i], list):
            resp = is_in_order([left[i]], right[i], tab_count + 1)
        elif isinstance(left[i], list) and isinstance(right[i], int):
            resp = is_in_order(left[i], [right[i]], tab_count + 1)
        if resp != None:
            return resp
    if len(left) < len(right):
        logger.debug("left ran out of items, in right order -> True")
        return True
    if len(left) > len(right):
        logger.debug("right ran out of items, out of order -> False")
        return False
    # hit end of lists, may need to continue
    return None


class Packet:
    def __init__(self, data: str | list) -> None:
        self.data: list = []
        if isinstance(data, str):
            self.data = eval(data)
        else:
            self.data = data

    def __str__(self) -> str:
        return str(self.data)

    def __lt__(self, __o: Packet) -> bool:
        return is_in_order(self.data, __o.data)


class Pair:
    def __init__(self, left: str, right: str) -> None:
        self.left = Packet(left)
        self.right = Packet(right)

    def is_in_order(self) -> bool:
        return self.left < self.right


class Signal:
    def __init__(self, data: str) -> None:
        self.pairs: list[Pair] = []
        for pair in data.split("\n\n"):
            (l, r) = pair.split("\n")
            self.pairs.append(Pair(l, r))

    def correct_order(self) -> list[bool]:
        return [p.is_in_order() for p in self.pairs]

    def correct_order_index(self) -> list[int]:
        return [o[0] + 1 for o in enumerate(self.correct_order()) if o[1] is True]

    def correct_order_sum(self) -> int:
        return sum(self.correct_order_index())


class Signal2:
    def __init__(self, data: str) -> None:
        self.packets: list[Packet] = []
        for pair in data.split("\n\n"):
            (l, r) = pair.split("\n")
            self.packets.append(Packet(l))
            self.packets.append(Packet(r))
        self.packets.append(Packet("[[2]]"))
        self.packets.append(Packet("[[6]]"))

    def sorted_packets(self) -> list:
        return [p.data for p in sorted(self.packets)]

    def divider_packets(self) -> list:
        sp = self.sorted_packets()
        return [
            sp.index([[2]]) + 1,
            sp.index([[6]]) + 1,
        ]

    def decoder_key(self) -> int:
        return reduce(lambda x, a: x * a, self.divider_packets())


def pt1(input: str) -> int:
    s = Signal(input)
    return s.correct_order_sum()


def pt2(input: str) -> int:
    s = Signal2(input)
    return s.decoder_key()


if __name__ == "__main__":
    with open("day13/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
