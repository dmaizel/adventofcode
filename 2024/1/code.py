def read_file():
    with open('./input.txt') as f:
        data = [*map(int, f.read().split())]
        return sorted(data[0::2]), sorted(data[1::2])

def part1(data):
    A, B = data
    return sum(map(lambda a, b: abs(a-b), A, B))

def part2(data):
    A, B = data
    return sum(map(lambda a, _: a * B.count(a), A, B))

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))

