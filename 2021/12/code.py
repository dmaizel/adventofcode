from collections import defaultdict


def read_file():
    neighbours = defaultdict(list)
    for line in open("input.txt"):
        a, b = line.strip().split("-")
        neighbours[a] += [b]
        neighbours[b] += [a]

    return neighbours


neighbours = read_file()
print(neighbours)


def count(part, seen=[], cave="start"):
    if cave == "end":
        return 1
    if cave in seen:
        if cave == "start":
            return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(count(part, seen + [cave], n) for n in neighbours[cave])


def part1():
    return count(part=1)


def part2():
    return count(part=2)


if __name__ == "__main__":
    print(part1())
    print(part2())
