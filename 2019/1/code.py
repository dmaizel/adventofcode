def read_file():
    with open('input.txt') as f:
        return list(map(int, f.read().strip().split('\n')))

def part1(requirements):
    return sum([x // 3 - 2 for x in requirements])

def part2(requirements):
    s = 0
    for req in requirements:
        while req > 0:
            res = part1([req])
            if res <= 0:
                break
            s += res
            req = res
    return s


requirements = read_file()
print(part1(requirements))
print(part2(requirements))
