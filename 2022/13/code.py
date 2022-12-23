from functools import cmp_to_key


def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n\n")


def read_file2():
    with open("input.txt") as f:
        return [eval(x) for x in list(filter(None, f.read().strip().split("\n")))]


def compare(x, y):
    if type(x) == str:
        x = eval(x)
    if type(y) == str:
        y = eval(y)
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])

    for a, b in zip(x, y):
        res = compare(a, b)
        if res != 0:
            return res

    return len(x) - len(y)


def part1(pairs):
    indices = []
    for pair_i, l in enumerate(pairs):
        a, b = l.split("\n")
        if compare(a, b) < 0:
            indices.append(pair_i + 1)
    return sum(indices)


def part2(pairs):
    indices = []
    compare_key = cmp_to_key(compare)
    pairs += [[[2]], [[6]]]
    res = sorted(pairs, key=compare_key)
    return (res.index([[2]]) + 1) * (res.index([[6]]) + 1)


if __name__ == "__main__":
    data = read_file()
    data2 = read_file2()
    print(part1(data))
    print(part2(data2))
