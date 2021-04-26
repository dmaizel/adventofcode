def read_file():
    with open('input.txt', 'r') as f:
        return [int(x) for x in f.read().strip()]

def solve(cups, full_len, moves):
    cup_list = {}

    for i in range(full_len):
        if i < len(cups) - 1:
            cup_list[cups[i]] = cups[i+1]
        elif i == len(cups) - 1 and len(cups) == full_len:
            cup_list[cups[i]] = cups[0]
        elif i == len(cups) - 1 and len(cups) < full_len:
            cup_list[cups[i]] = max(cups) + 1
        elif i < full_len - 1:
            cup_list[i + 1] = i + 2
        elif i == full_len - 1:
            cup_list[i + 1] = cups[0]

    min_cup = min(cup_list)
    ptr = cups[0]
    for _ in range(moves):
        # remove 3 cups
        c1 = cup_list[ptr]
        c2 = cup_list[c1]
        c3 = cup_list[c2]
        cup_list[ptr] = cup_list[c3]

        # find dest
        # decremnting 2 because the lowest cup can be 1 and not 0
        dest = ((ptr - 1 - min_cup) % full_len) + min_cup
        while dest in [c1, c2, c3]:
            dest = ((dest - 1 - min_cup) % full_len) + min_cup

        # reinsert cups after dest
        cup_list[c3] = cup_list[dest]
        cup_list[dest] = c1

        # move ptr forward
        ptr = cup_list[ptr]

    return cup_list

def part1(cups):
    cups = solve(cups, len(cups), 100)
    res = ''
    next_cup = cups[1]
    while next_cup != 1:
        res += str(next_cup)
        next_cup = cups[next_cup]

    return res

def part2(cups):
    cups = solve(cups, 1000000, 10000000)
    next_cup = cups[1]
    return next_cup * cups[next_cup]

if __name__ == '__main__':
    cups = read_file()
    print(part1(cups))
    print(part2(cups))
