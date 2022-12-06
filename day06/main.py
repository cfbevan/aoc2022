class ComDevice():

    def __init__(self, stream: str = '') -> None:
        self.stream = stream
        self.window = 4

    def find_start_of_packet(self) -> int | None:
        for index in range(0, len(self.stream) - (self.window - 1)):
            window = self.stream[index : index + self.window]
            if len(window) == len(set(window)):
                return index + self.window
        return None


def pt1(input: str) -> str:
    cd = ComDevice(input)
    return cd.find_start_of_packet()

def pt2(input: str) -> str:
    cd = ComDevice(input)
    cd.window = 14
    return cd.find_start_of_packet()

if __name__ == '__main__':
    with open('day06/input.txt', 'r') as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
