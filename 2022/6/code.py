def read_file():
    with open("input.txt") as f:
        return f.read().strip()

def solve(data, n):
    for i in range(len(data)):
        seq = data[i: i+n]
        if len(set(seq)) == len(seq):
            return i + n
    return -1

def part1(data):
    return solve(data, 4)

def part2(data):
    return solve(data, 14)

if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
