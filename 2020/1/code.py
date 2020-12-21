#!/user/bin/env python3

inp = "input1.txt"
numbers = list(map(lambda x: int(x) ,open(inp).read().strip().split('\n')))


def part_one():
    for num in numbers:
        if 2020-num in numbers:
            return (2020-num) * num   

def part_two():
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            k = 2020 - numbers[i] - numbers[j]
            if k in numbers:
                return numbers[i] * numbers[j] * k


if __name__ == '__main__':
    print(part_one())
    print(part_two())
