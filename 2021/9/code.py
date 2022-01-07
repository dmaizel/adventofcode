import os
import math


def read_file():
    heights = {}
    with open(f"{os.curdir}/input.txt") as f:
        for y, l in enumerate(f):
            for x, h in enumerate(l.strip()):
                heights[(x, y)] = int(h)
    return heights
    # return {
    #     (x, y): int(h) for y, l in enumerate(f) for x, h in enumerate(l.strip())
    # }


heights = read_file()


def neighbours(x, y):
    return filter(
        lambda n: n in heights,  # remove points
        [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)],
    )  #  outside grid


def is_low(p):
    return all(heights[p] < heights[n] for n in neighbours(*p))


def part1():
    low_points = list(filter(is_low, heights))
    return sum(heights[p] + 1 for p in low_points)


def count_basin(p):
    if heights[p] == 9:
        return 0
    del heights[p]
    return 1 + sum(map(count_basin, neighbours(*p)))


def part2():
    low_points = list(filter(is_low, heights))
    basins = [count_basin(p) for p in low_points]
    return math.prod(sorted(basins)[-3:])


if __name__ == "__main__":
    print(part1())
    print(part2())
