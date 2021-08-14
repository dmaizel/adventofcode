def read_file():
    with open('input.txt') as f:
        return f.read().split('-')

def is_not_dec(num):
    minn = num[0]
    for d in num:
        if int(d) < int(minn):
            return False
        minn = d
    return True

def two_equal_adj(num):
    prev_num = -1
    for d in num:
        if int(d) == int(prev_num):
            return True
        prev_num = d

    return False


def only_two_equal_adj(num):
    prev_num = -1
    adj = {}
    for d in num:
        if int(d) == int(prev_num):
            if d in adj:
                adj[d] = False
            else:
                adj[d] = True
        prev_num = d

    return True in adj.values()


def part1(data):
    return sum(1 for i in range(int(data[0]), int(data[1])) if is_not_dec(str(i)) and two_equal_adj(str(i)))

def part2(data):
    return sum(1 for i in range(int(data[0]), int(data[1])) if is_not_dec(str(i)) and only_two_equal_adj(str(i)))

data = read_file()
print(part1(data))
print(part2(data))
