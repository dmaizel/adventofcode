from collections import deque


def read_file():
    with open("input.txt") as f:
        return [list(x) for x in f.read().strip().splitlines()]


def get_start_and_end(grid):
    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == "S":
                start_c = c
                start_r = r
                grid[r][c] = "a"
            elif item == "E":
                end_r = r
                end_c = c
                grid[r][c] = "z"
    return ((start_r, start_c), (end_r, end_c))


def part1():
    grid = read_file()
    (start_r, start_c), (end_r, end_c) = get_start_and_end(grid)

    q = deque()
    q.append((0, start_r, start_c))

    visited = {(start_r, start_c)}

    while q:
        d, r, c = q.popleft()
        for next_r, next_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                next_r < 0
                or next_c < 0
                or next_r >= len(grid)
                or next_c >= len(grid[0])
            ):
                continue
            if (next_r, next_c) in visited:
                continue
            if ord(grid[next_r][next_c]) - ord(grid[r][c]) > 1:
                continue
            if next_r == end_r and next_c == end_c:
                return d + 1
            visited.add((next_r, next_c))
            q.append((d + 1, next_r, next_c))


def part2():
    grid = read_file()
    (_, _), (end_r, end_c) = get_start_and_end(grid)

    q = deque()
    q.append((0, end_r, end_c))

    visited = {(end_r, end_c)}
    starts = set()

    while q:
        d, r, c = q.popleft()
        for next_r, next_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                next_r < 0
                or next_c < 0
                or next_r >= len(grid)
                or next_c >= len(grid[0])
            ):
                continue
            if (next_r, next_c) in visited:
                continue
            if ord(grid[r][c]) - ord(grid[next_r][next_c]) > 1:
                continue
            if grid[next_r][next_c] == "a":
                return d + 1
            visited.add((next_r, next_c))
            q.append((d + 1, next_r, next_c))

    return min(starts)


if __name__ == "__main__":
    print(part1())
    print(part2())
