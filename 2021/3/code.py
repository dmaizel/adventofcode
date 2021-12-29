def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")


def part1(data):
    gamma = epsilon = ""
    l = len(data[0])
    for i in range(l):
        l = [x[i] for x in data]
        gamma += max(l, key=l.count)
        epsilon += min(l, key=l.count)

    return int(gamma, 2) * int(epsilon, 2)


def get_most_common(l):
    zero_count = l.count("0")
    one_count = l.count("1")
    return "1" if one_count >= zero_count else "0"


def get_least_common(l):
    zero_count = l.count("0")
    one_count = l.count("1")
    return "0" if zero_count <= one_count else "1"


def part2(data):
    ox_list = data
    co_list = data
    for i in range(len(data[0])):
        ox_l = [x[i] for x in ox_list]
        co_l = [x[i] for x in co_list]
        most_common = get_most_common(ox_l)
        least_common = get_least_common(co_l)
        if len(ox_list) == 1 and len(co_list) == 1:
            break
        if len(ox_list) > 1:
            ox_list = [x for x in ox_list if x[i] == most_common]
        if len(co_list) > 1:
            co_list = [x for x in co_list if x[i] == least_common]

    return int(ox_list[0], 2) * int(co_list[0], 2)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
