from functools import reduce  # Required in Python 3
import operator
import sys
sys.set_int_max_str_digits(999999999)

def read_file():
    with open("test_input.txt") as f:
        return f.read().strip().split("\n\n")


def part1(data, rounds):
    monkey_items = {}
    inspected = {}
    for i in range(rounds):
        for monkey in data:
            lines = monkey.split('\n')
            monkey_num = int(lines[0].split()[1][: -1])
            items = list(map(int, lines[1].split(':')[1].split(',')))
            if_true = int(lines[-2].split()[-1])
            if_false = int(lines[-1].split()[-1])
            test = lambda x : x % int(lines[3].split()[-1]) == 0
            operation = lines[2].split('=')[1].strip()
            if i != 0:
                items = []
            if monkey_num in monkey_items:
                items.extend(monkey_items[monkey_num])
                monkey_items[monkey_num] = []
            for item in items:
                if monkey_num not in inspected:
                    inspected[monkey_num] = 0
                inspected[monkey_num] += 1
                worry_level = int(eval(operation.replace('old', str(item)))) // 3
                to = if_true if test(worry_level) else if_false
                if to not in monkey_items:
                    monkey_items[to] = []
                monkey_items[to].append(worry_level)
    return reduce(operator.mul,sorted(inspected.values(), reverse=True)[0:2])

def part2(data, rounds):
    monkey_items = {}
    inspected = {}
    N = 1
    for i in range(rounds):
        for monkey in data:
            lines = monkey.split('\n')
            monkey_num = int(lines[0].split()[1][: -1])
            items = list(map(int, lines[1].split(':')[1].split(',')))
            if_true = int(lines[-2].split()[-1])
            if_false = int(lines[-1].split()[-1])
            test_num = int(lines[3].split()[-1])
            if i == 0:
                N *= test_num
            test = lambda x : x % test_num == 0
            
            operation = lines[2].split('=')[1].strip()
            if i != 0:
                items = []
            if monkey_num in monkey_items:
                items.extend(monkey_items[monkey_num])
                monkey_items[monkey_num] = []
            for item in items:
                if monkey_num not in inspected:
                    inspected[monkey_num] = 0
                inspected[monkey_num] += 1
                worry_level = int(eval(operation.replace('old', str(item))))
                worry_level %= N
                to = if_true if test(worry_level) else if_false
                if to not in monkey_items:
                    monkey_items[to] = []
                monkey_items[to].append(worry_level)
    print(sorted(inspected.values(), reverse=True))
    return reduce(operator.mul,sorted(inspected.values(), reverse=True)[0:2])


def bla():
    pass


if __name__ == "__main__":
    data = read_file()
    print(part1(data, 20))
    print(part2(data, 10000))
