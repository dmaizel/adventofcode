def read_file():
    with open("input.txt") as f:
        return f.read().strip().split()


def part1(data):
    trees = 0
    grid = [list(map(int, list(line))) for line in data]

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            if all(grid[r][x] < k for x in range(c)) or all (grid[r][x] < k for x in range(c+1, len(grid[r]))) or all(grid[x][c] < k for x in range(r)) or all(grid[x][c] < k for x in range(r+1, len(grid))):
                trees += 1

    return trees

def part2(data):
    grid = [list(map(int, list(line))) for line in data]
    m = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            L = R = U = D = 0
            for x in range(c - 1, -1, -1):
                L += 1
                if grid[r][x] >= k:
                    break
            for x in range(c + 1, len(grid[r])):
                R += 1
                if grid[r][x] >= k:
                    break
            for x in range(r + 1, len(grid)):
                D += 1
                if grid[x][c] >= k:
                    break
            for x in range(r - 1, -1, -1):
                U += 1
                if grid[x][c] >= k:
                    break
            m = max(m, L * R * U * D)

    return m

if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))

