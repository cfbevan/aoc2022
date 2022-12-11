from math import prod


class Monkey:
    def __init__(self, data: str):
        lines = data.strip().split("\n")
        self.id = int(lines[0].split()[1].strip(":"), 10)
        self.items = [
            int(x.strip(), 10) for x in lines[1].strip().split(":")[1].split(",")
        ]
        val = lines[2].split(" ")[-1]
        if "+" in lines[2] and val == "old":
            self.operation = lambda x: x + x
            self.operation_str = f"increased by {val}"
        elif "+" in lines[2]:
            self.operation = lambda x: x + int(val, 10)
            self.operation_str = f"increased by {val}"
        elif "*" in lines[2] and val == "old":
            self.operation = lambda x: x * x
            self.operation_str = f"multiplied by {val}"
        elif "*" in lines[2]:
            self.operation = lambda x: x * int(val, 10)
            self.operation_str = f"multiplied by {val}"
        self.test = int(lines[3].split(" ")[-1], 10)
        self.test_true = int(lines[4].split(" ")[-1], 10)
        self.test_false = int(lines[5].split(" ")[-1], 10)
        self.inspections = 0

    def __str__(self):
        return f"Monkey{self.id}(inspections={self.inspections},items={self.items})"

    def inspect(self, mod: int, div_worry: bool, debug: bool) -> int:
        if debug:
            print(f"  Monkey inspects an item with worry level of {self.items[0]}.")
        self.inspections += 1
        self.items[0] = self.operation(self.items[0]) % mod
        if debug:
            print(f"    Worry level is {self.operation_str} to {self.items[0]}.")
        if div_worry:
            self.items[0] = self.items[0] // 3
            if debug:
                print(
                    f"    Monkey gets bored with item. Worry level is divided by 3 to {self.items[0]}."
                )
        if self.items[0] % self.test == 0:
            if debug:
                print(f"    Current worry level is divisible by {self.test}.")
                print(
                    f"    Item with worry level {self.items[0]} is thrown to monkey {self.test_true}."
                )
            return self.test_true
        else:
            if debug:
                print(f"    Current worry level is not divisible by {self.test}.")
                print(
                    f"    Item with worry level {self.items[0]} is thrown to monkey {self.test_false}."
                )
            return self.test_false

    def catch_item(self, item: int):
        self.items.append(item)


class MitM:
    def __init__(self, data: str) -> None:
        self.monkeys: list[Monkey] = []
        for m_data in data.split("\n\n"):
            self.monkeys.append(Monkey(m_data))
        self.mod = prod([m.test for m in self.monkeys])

    def run(
        self, iterations: int, div_worry: bool, debug: int = False
    ) -> tuple[int, int]:
        for round in range(iterations):
            if debug > 1:
                print(f"== Round {round} ==")
            for m in self.monkeys:
                if debug > 1:
                    print(f"Monkey {m.id}:")
                for _ in range(len(m.items)):
                    res = m.inspect(self.mod, div_worry, debug > 1)
                    self.monkeys[res].catch_item(m.items.pop(0))
            if debug > 0:
                print(f"== After round {round} ==")
                for m in self.monkeys:
                    print(f"Monkey {m.id} inspected items {m.inspections} times.")

        inspections = sorted([m.inspections for m in self.monkeys])
        return (inspections[-1], inspections[-2])


def pt1(input: str) -> str:
    mitm = MitM(input)
    active = mitm.run(20, div_worry=True)
    return str(active[0] * active[1])


def pt2(input: str) -> str:
    mitm = MitM(input)
    active = mitm.run(10000, div_worry=False)
    return str(active[0] * active[1])


if __name__ == "__main__":
    with open("day11/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
