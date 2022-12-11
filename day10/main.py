from typing import Generator


class CRT:
    def __init__(self) -> None:
        self.x = 1
        self.cycle = 0
        self.width = 40
        self.lit = "#"
        self.dark = "."
        self.screen = []
        self.row = ""

    @property
    def signal_strength(self) -> int:
        return self.cycle * self.x

    def draw_pixel(self) -> None:
        y = (self.cycle - 1) % self.width
        if self.x - 1 <= y <= self.x + 1:
            self.row += self.lit
        else:
            self.row += self.dark
        if len(self.row) == self.width:
            self.screen.append(self.row)
            self.row = ""

    def draw_screen(self) -> None:
        print("\n".join("".join(row) for row in self.screen))

    def _debug_start(self, inst: str, debug: bool):
        if debug:
            print(f"Start cycle {self.cycle}: Begin executing {inst}")
            print(
                f"Sprite position: {''.join(['#' if self.x -1 <= s  <= self.x + 1 else '.' for s in range(self.width)])}"
            )
            print(
                f"During cycle {self.cycle}: CRT draws pixel in position {len(self.row)}"
            )
            print(f"Current CRT row: {self.row}")
            print("\n")

    def _debug_during(self, debug: bool):
        if debug:
            print(
                f"Sprite position: {''.join(['#' if self.x -1 <= s  <= self.x + 1 else '.' for s in range(self.width)])}"
            )
            print(
                f"During cycle {self.cycle}: CRT draws pixel in position {len(self.row)}"
            )
            print(f"Current CRT row: {self.row}")

    def _debug_end(self, inst: str, debug: bool):
        if debug:
            print(
                f"End of cycle {self.cycle}: finish executing {inst} (Register X is now {self.x})"
            )
            self.draw_screen()
            print(self.row)
            print(f"\n")

    def tick(self):
        self.cycle += 1
        self.draw_pixel()

    def run(
        self, input: str, debug: bool = False
    ) -> Generator[tuple[int, int, int], None, None]:
        """Get signal strength at 20 and every 40 after that.

        Args:
            input (str): Instruction set.

        Yields:
            Generator[int, None, None]: Cycle, Signal Strength
        """
        if debug:
            print(
                f"Sprite position: {''.join(['#' if self.x -1 <= s  <= self.x + 1 else '.' for s in range(self.width)])}"
            )
            print("\n")
        for inst in input.split("\n"):
            match inst.strip().split():
                case ["addx", amt]:
                    self.tick()
                    self._debug_start(inst, debug)
                    if (self.cycle - 20) % 40 == 0:
                        yield (self.cycle, self.x, self.signal_strength)
                    self.tick()
                    if (self.cycle - 20) % 40 == 0:
                        yield (self.cycle, self.x, self.signal_strength)
                    self._debug_during(debug)
                    self.x += int(amt, 10)
                case ["noop"]:
                    self.tick()
                    self._debug_start(inst, debug)
                    if (self.cycle - 20) % 40 == 0:
                        yield (self.cycle, self.x, self.signal_strength)
                case _:
                    print(f"Unknown Command: {inst}")
            self._debug_end(inst, debug)
        if debug:
            self.draw_screen()


def pt1(input: str) -> str:
    c = CRT()
    return sum(x[2] for x in c.run(input))


def pt2(input: str) -> None:
    c = CRT()
    list(c.run(input))
    c.draw_screen()


if __name__ == "__main__":
    with open("day10/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        pt2(input)
