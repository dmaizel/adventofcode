def read_file():
    grid = {}
    with open("input.txt") as f:
        for y, l in enumerate(f):
            for x, energy in enumerate(l.strip()):
                grid[(x, y)] = int(energy)
    return grid


def neighbours(grid, x, y):
    return filter(
        grid.get,
        [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 1),
        ],
    )


def part1(grid):
    count = 0
    grid = grid.copy()
    for _ in range(100):
        for i in grid:
            grid[i] += 1
        flashing = {i for i in grid if grid[i] > 9}

        while flashing:
            f = flashing.pop()
            grid[f] = 0
            count += 1
            for n in neighbours(grid, *f):
                grid[n] += 1
                if grid[n] > 9:
                    flashing.add(n)
    return count


def part2(grid):
    count = 0
    grid = grid.copy()
    for step in range(1, 1000):
        for i in grid:
            grid[i] += 1
        flashing = {i for i in grid if grid[i] > 9}

        while flashing:
            f = flashing.pop()
            grid[f] = 0
            count += 1
            for n in neighbours(grid, *f):
                grid[n] += 1
                if grid[n] > 9:
                    flashing.add(n)
        if sum(grid.values()) == 0:
            return step


if __name__ == "__main__":
    data = read_file()
    print(data)
    print(part1(data))
    print(part2(data))
