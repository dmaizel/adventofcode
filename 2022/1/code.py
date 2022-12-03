def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n\n")

def part1(data):
    return max([sum([int(num) for num in x.split('\n')]) for x in [i for i in data]])


def part2(data):
    return sum(sorted(([sum([int(num) for num in x.split('\n')]) for x in [i for i in data]]), reverse=True)[0:3])

if __name__ == "__main__":
    inventories = read_file()
    print(part1(inventories))
    print(part2(inventories))
