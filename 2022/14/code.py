def read_file():
    with open("input.txt") as f:
        return f.read().strip().splitlines()


def part1(data):
    blocked = set()
    abyss = 0
    for line in data:
        pairs = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        for i in range(len(pairs) - 1):
            x1, y1 = pairs[i]
            x2, y2 = pairs[i + 1]
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    blocked.add(x + y * 1j)
                    abyss = max(abyss, y + 1)

    total = 0
    while True:
        s = 500
        while True:
            if s.imag >= abyss:
                return total
            if s + 1j not in blocked:
                s += 1j
                continue
            if s + 1j - 1 not in blocked:
                s += 1j - 1
                continue
            if s + 1j + 1 not in blocked:
                s += 1j + 1
                continue
            blocked.add(s)
            total += 1
            break


def part2(data):
    blocked = set()
    abyss = 0
    for line in data:
        pairs = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        for i in range(len(pairs) - 1):
            x1, y1 = pairs[i]
            x2, y2 = pairs[i + 1]
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    blocked.add(x + y * 1j)
                    abyss = max(abyss, y + 1)

    total = 0
    while 500 not in blocked:
        s = 500
        while True:
            if s.imag >= abyss:
                break
            if s + 1j not in blocked:
                s += 1j
                continue
            if s + 1j - 1 not in blocked:
                s += 1j - 1
                continue
            if s + 1j + 1 not in blocked:
                s += 1j + 1
                continue
            break
        blocked.add(s)
        total += 1
    return total


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
