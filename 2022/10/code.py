def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")


def solve(data):
    cycle_to_value = {}
    value = 1
    cycle = 1
    for instruction in data:
        cycle += 1
        cycle_to_value[cycle] = value
        if instruction.split()[0] == "noop":
            continue
        else:
            cycle += 1
            value += int(instruction.split()[1])
            cycle_to_value[cycle] = value
            continue

    return cycle_to_value


def part1(data):
    cycle_to_value = solve(data)
    return sum([i * cycle_to_value[i] for i in range(20, len(cycle_to_value), 40)])


def part2(data):
    cycle_to_value = {}
    value = 1
    cycle = 1
    sprite = ""
    for instruction in data:
        if (cycle - 1) % 40 in [value - 1, value, value + 1]:
            sprite += "#"
        else:
            sprite += "."
        cycle += 1
        cycle_to_value[cycle] = value
        if instruction.split()[0] == "noop":
            continue
        else:
            if (cycle - 1) % 40 in [value - 1, value, value + 1]:
                sprite += "#"
            else:
                sprite += "."
            cycle += 1
            value += int(instruction.split()[1])
            cycle_to_value[cycle] = value
            continue

    line = ""
    i = 0
    for v in sprite:
        line += v
        i += 1
        if i == 40:
            print(line)
            i = 0
            line = ""


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
