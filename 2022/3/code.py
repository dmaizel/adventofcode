from functools import reduce

def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")

def get_common(*args):
    return reduce(lambda a, b: a & b, [set(arg) for arg in args]).pop()

def get_priority(x):
    if (x.isupper()):
        return ord(x) - ord('A') + 1 + 26
    return ord(x) - ord('a') + 1

def part1(data):
    sum = 0
    for line in data:
        first, second = line[:len(line) // 2], line[len(line) // 2:]
        common = get_common(first, second)
        sum += get_priority(common)

    return sum

def part2(data):
    sum = 0
    data = [data[i:i+3] for i in range(0, len(data), 3)]
    for batch in data:
        common = get_common(batch[0], batch[1], batch[2])
        sum += get_priority(common)
    return sum

if __name__ == "__main__":
    lines = read_file()
    print(part1(lines))
    print(part2(lines))
