def read_file():
    with open("input.txt") as f:
        return list(map(int, f.read().strip().split(",")))


def part1(data):
    opts = []
    for pos in range(min(data), max(data)):
        opts.append(sum([abs(x - pos) for x in data]))
    return min(opts)
    # return min([sum([abs(x - pos) for x in data]) for pos in data])


def part2(data):
    opts = []
    for pos in range(min(data), max(data)):
        opts.append(sum([sum(list(range(abs(x - pos) + 1))) for x in data]))

    return min(opts)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
