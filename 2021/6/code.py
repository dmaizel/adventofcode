def read_file():
    with open("input.txt") as f:
        return list(map(int, f.read().strip().split(",")))


def solve(data, days):
    current_state = {
        0: data.count(0),
        1: data.count(1),
        2: data.count(2),
        3: data.count(3),
        4: data.count(4),
        5: data.count(5),
        6: data.count(6),
        7: data.count(7),
        8: data.count(8),
    }

    for _ in range(days):
        next_state = {
            0: current_state[1],
            1: current_state[2],
            2: current_state[3],
            3: current_state[4],
            4: current_state[5],
            5: current_state[6],
            6: current_state[7],
            7: current_state[8],
            8: current_state[0],
        }
        if current_state[0] > 0:
            next_state[6] += current_state[0]

        current_state = next_state

    return sum(current_state.values())


def part1(data):
    return solve(data, 80)


def part2(data):
    return solve(data, 256)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
