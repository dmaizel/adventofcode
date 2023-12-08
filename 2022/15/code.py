import re


def read_file():
    with open("input.txt") as f:
        return f.read().strip().splitlines()


def part1(data):
    pattern = re.compile(r"-?\d+")
    for line in data:
        sx, sy, bx, by = map(int, pattern.findall(line))


if __name__ == "__main__":
    data = read_file()
    print(data)
