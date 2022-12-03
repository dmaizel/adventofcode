from heapq import heappop, heappush
from typing import NewType
import math


def read_file():
    grid = {}
    with open("input.txt") as f:
        for y, line in enumerate(f):
            for x, risk_level in enumerate(line.strip()):
                grid[(int(x), int(y))] = int(risk_level)
    return grid


def solve(grid, times):
    heap = [(0, 0, 0)]
    SetOfCords = NewType('SetOfCords', set[tuple[int, int]])
    seen = SetOfCords({(0,0)})
    L = math.sqrt(len(grid))
    l = times * L - 1

    while heap:
        distance, x, y = heappop(heap)

        if x == l and y == l:
            return distance

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_y < 0 or new_x >= times * L or new_y >= times * L:
                continue            
            a, am = divmod(new_x, L)
            b, bm = divmod(new_y, L)
            n = (grid[(am, bm)] + a + b - 1) % 9 + 1

            if (new_x, new_y) not in seen:
                seen.add((new_x, new_y))
                heappush(heap, (distance + n, new_x, new_y))


def part1(data):
    return solve(data, 1)


def part2(data):
    return solve(data, 5)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))

