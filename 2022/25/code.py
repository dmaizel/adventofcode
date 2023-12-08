def read_file():
    with open("input.txt") as f:
        return f.read().strip().splitlines()


def snafu_to_dec(num):
    total = 0
    coef = 1
    for x in reversed(num):
        total += ("=-012".find(x) - 2) * coef
        coef *= 5
    return total

def part1(data):
    total = 0
    for line in data:
        total += snafu_to_dec(line)
    return total

if __name__ == "__main__":
    data = read_file()
    # print(data)
    # print(snafu_to_dec('10'))
    print(part1(data))
