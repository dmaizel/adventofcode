def read_file():
    with open('input.txt') as f:
        return [[int(y) for y in x.split(' ')] for x in f.read().strip().split('\n')]

def is_safe(row):
    inc = {row[i+1] - row[i] for i in range(len(row) - 1)}
    return inc <= {1,2,3} or inc <= {-1, -2, -3}

def part1(data):
    return sum([is_safe(row) for row in data])

def part2(data):
    return sum([any([is_safe(row[:i] + row[i+1:]) for i in range(len(row))]) for row in data])

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))
