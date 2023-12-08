def read_file():
    with open("test_input.txt") as f:
        return f.read().strip().split("\n")


def exec_moves(moves, num_knots):
    knots = [(0, 0)] * num_knots
    visited_positions = {(0, 0)}
    for move in moves:
        ((dx, dy), steps) = move
        for _ in range(steps):
            (hx, hy) = knots[0]
            knots[0] = hx + dx, hy + dy
            for i in range(len(knots) - 1):
                [(hx, hy), (tx, ty)] = knots[i:i+2]


def part1(data):
    moves = [
        ({"R": (0, 1), "U": "-1, 0", "L": (0, -1), "D": (1, 0)}[line[0]], int(line[2:]))
        for line in data
    ]
    print(moves)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
