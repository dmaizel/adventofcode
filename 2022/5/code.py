def read_file():
    with open("input.txt") as f:
        return f.read().split("\n\n")


def part1(crates, instructions):
    num_crates = int(crates.strip()[-1])
    crates = crates.split("\n")[:-1]
    stacks = [[] for _ in range(num_crates)]

    for row in reversed(crates):
        creates = row[1::4]
        for i, crate in enumerate(creates):
            if crate != " ":
                stacks[i].append(crate)

    for step in instructions.strip().split("\n"):
        nums = list(map(int, list(filter(lambda x: x.isdigit(), step.split(" ")))))
        num, _from, to = nums
        for i in range(num):
            p = stacks[_from - 1].pop()
            stacks[to - 1].append(p)

    return "".join([s.pop() for s in stacks])


def part2(crates, instructions):
    num_crates = int(crates.strip()[-1])
    crates = crates.split("\n")[:-1]
    stacks = [[] for _ in range(num_crates)]

    for row in reversed(crates):
        creates = row[1::4]
        for i, crate in enumerate(creates):
            if crate != " ":
                stacks[i].append(crate)

    for step in instructions.strip().split("\n"):
        nums = list(map(int, list(filter(lambda x: x.isdigit(), step.split(" ")))))
        num, _from, to = nums
        to_move = stacks[_from - 1][len(stacks[_from - 1]) - num :]
        stacks[_from - 1] = stacks[_from - 1][0 : len(stacks[_from - 1]) - num]
        stacks[to - 1].extend(to_move)

    return "".join([s.pop() for s in stacks])


if __name__ == "__main__":
    data = read_file()
    crates, instructions = data
    print(part1(crates, instructions))
    print(part2(crates, instructions))
