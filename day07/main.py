from typing import Type, Protocol


class FSObject(Protocol):
    name: str

    def size(self, cache: dict[str, int] | None = None) -> int:
        ...

    def get_path(self) -> str:
        ...


class File(FSObject):
    def __init__(self, name: str, parent: Type["Directory"], size: int):
        self.name = name
        self.parent = parent
        self._size = size

    def get_path(self) -> str:
        return f"{self.parent.get_path()}/{self.name}"

    def size(self, cache: dict[str, int] | None = None) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.name} (file, size={self.size})"


class Directory:
    def __init__(self, name: str, parent: Type["Directory"] | None = None) -> None:
        self.name = name
        self.parent = parent
        self.children: list[FSObject] = []

    def add_child(self, child: FSObject):
        self.children.append(child)

    def get_path(self) -> str:
        if self.parent is None:
            return self.name
        return f"{self.parent.get_path}/{self.name}"

    def get_child(self, name: str) -> FSObject:
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError

    def __iter__(self):
        for child in self.children:
            if not hasattr(child, "children"):
                yield child.name, child.size()
            else:
                yield child.name, dict(child)

    def size(self, cache: dict[str, int] | None = None) -> int:
        curr_path = self.get_path()
        total_size = sum(child.size(cache) for child in self.children)
        if cache is not None:
            cache[curr_path] = total_size
        return total_size

    def __repr__(self):
        return f"{self.name} (dir)"


class ComSystem:
    def __init__(self) -> None:
        self.filesystem = Directory("/")
        self.current_directory = self.filesystem

    def _cd(self, directory: str) -> None:
        match directory:
            case "/":
                self.current_directory = self.filesystem
            case "..":
                self.current_directory = self.current_directory.parent
            case _:
                self.current_directory = self.current_directory.get_child(directory)

    def _ls_output(self, size_or_dir: str, name: str) -> None:
        if size_or_dir == "dir":
            self.current_directory.add_child(Directory(name, self.current_directory))
        else:
            self.current_directory.add_child(
                File(name, self.current_directory, int(size_or_dir))
            )

    def run(self, commands: str) -> None:
        for command in commands.split("\n"):
            command = command.strip().split()
            match command:
                case ("$", "cd", "/"):
                    self._cd("/")
                case ("$", "cd", ".."):
                    self._cd("..")
                case ("$", "cd", path):
                    self._cd(path)
                case ("$", "ls"):
                    pass
                case (size_or_dir, name):
                    self._ls_output(size_or_dir, name)

    def get_dir_sizes(self) -> dict[str, int]:
        all_dirs = {}
        if self.filesystem.get_path() in all_dirs:
            return all_dirs
        self.filesystem.size(all_dirs)
        return all_dirs

    def get_small_dirs(self, under: int) -> dict[str, int]:
        return [v for v in self.get_dir_sizes().values() if v < under]


def pt1(input: str) -> str:
    cs = ComSystem()
    cs.run(input)
    return sum(cs.get_small_dirs(100000))


def pt2(input: str) -> str:
    total_space = 70000000
    need = 30000000
    cs = ComSystem()
    cs.run(input)
    dir_sizes = {}
    used = cs.filesystem.size(dir_sizes)
    return min(
        [size for size in dir_sizes.values() if total_space - used + size >= need]
    )


if __name__ == "__main__":
    with open("day07/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
