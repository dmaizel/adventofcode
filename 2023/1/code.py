import re

def read_file():
    with open('input.txt') as f:
        return f.read().splitlines()

def part1(data):
    sum = 0
    for line in data:
        first_num = None
        last_num = None
        for ch in line:
            if ch.isdigit():
                if first_num is None:
                    first_num = ch
                last_num = ch
        sum += int(first_num + last_num)

    return sum



def part2(data):
    for i, line in enumerate(data):
        data[i] = line.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine')
    return part1(data)

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))
