from functools import reduce
import operator


def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")


def part1(data):
    sum = 0
    for pair in data:
        first, second = pair.split(',')
        a, b = map(int, first.split('-'))
        c, d = map(int, second.split('-'))
        if (c >= a and d <= b) or (c <= a and d >= b):
            sum += 1
    return sum


def part2(data):
    sum = 0
    for pair in data:
        first, second = pair.split(',')
        a, b = map(int, first.split('-'))
        c, d = map(int, second.split('-'))

        fpmax, spmax = max(a, b), max(c, d)
        fpmin, spmin = min(a, b), min(c, d)
        if (
            spmin <= fpmax <= spmax
            or fpmin <= spmax <= fpmax
            or spmin <= fpmin <= spmax
            or fpmin <= spmin <= fpmax
        ):
            sum += 1
    return sum


if __name__ == "__main__":
    pairs = read_file()
    print(part1(pairs))
    print(part2(pairs))
