def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")


def sum_of_next(size, arr):
    return sum([int(x) for x in arr[:size]])


def solve(data, size):
    prev = float("-inf")
    counter = 0
    for i in range(1, len(data)):
        if len(data[i:]) < size:
            break
        curr = int(sum_of_next(size, data[i:]))
        if curr > prev:
            counter += 1
        prev = curr
    return counter


def part1(data):
    return solve(data, 1)


def part2(data):
    return solve(data, 3)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
