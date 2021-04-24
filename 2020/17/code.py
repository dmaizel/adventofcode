from itertools import product

def print_grid(l):
    for line in l:
        print(line)

def read_file():
    with open('input.txt') as f:
        return f.read().strip().split('\n')

def get_active_cells(lines):
    active_cells = set()
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell == '#':
                active_cells.add((x, y, 0, 0))
    return active_cells

def get_neighbors_count(point, cells):
    num_of_dim = len(point)
    diffs = product([-1, 0, 1], repeat=num_of_dim)

    return sum(
        [
            tuple([x1 + x2 for x1, x2 in zip(d, point)]) in cells
            for d in diffs
            if d != tuple([0] * num_of_dim)
        ]
    )

def get_bounds(cells):
    res = []
    for i in range(4):
        res.append(min(cells, key=lambda x: x[i])[i] - 1)
        res.append(max(cells, key=lambda x: x[i])[i] + 2)
    return res

def step(cells, num_of_dim):
    bounds = get_bounds(cells)
    next_cells = set()
    w_range = [0] if num_of_dim == 3 else range(bounds[6], bounds[7])
    for x in range(bounds[0], bounds[1]):
        for y in range(bounds[2], bounds[3]):
            for z in range(bounds[4], bounds[5]):
                for w in w_range:
                    ns = get_neighbors_count((x, y, z, w), cells)
                    if (x, y, z, w) in cells and (ns == 2 or ns ==3):
                        next_cells.add((x, y, z, w))
                    elif (x, y, z, w) not in cells and ns == 3:
                        next_cells.add((x, y, z, w))
    return next_cells

def solve(data, num_of_dim):
    cells = get_active_cells(data)
    for _ in range(6):
        cells = step(cells, num_of_dim)

    return len(cells)

def part1(data):
    return solve(data, 3)

def part2(data):
    return solve(data, 4)

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))
