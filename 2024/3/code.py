import re

def read_file():
    with open('input.txt') as f:
        return f.read()

def part1(data):
    return sum([int(x)*int(y) for x,y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)])

def part2(data):
    enabled = True
    sum = 0

    for x, y, do, dont in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", data):
        if do or dont:
            enabled = bool(do)
        else:
            x = int(x) * int(y)
            if enabled:
                sum += x
    return sum

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))
