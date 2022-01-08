from collections import Counter


def read_file():
    with open("input.txt") as f:
        template, _, *rules = f.read().strip().split("\n")
        rules = dict(rule.split(" -> ") for rule in rules)
        pairs = Counter(map(str.__add__, template, template[1:]))
        chars = Counter(template)
        return rules, pairs, chars


def solve(data, steps):
    rules, pairs, chars = data
    rules = rules.copy()
    pairs = pairs.copy()
    chars = chars.copy()

    for _ in range(steps):
        for (a, b), c in pairs.copy().items():
            x = rules[a + b]
            pairs[a + b] -= c
            pairs[a + x] += c
            pairs[x + b] += c
            chars[x] += c
    return max(chars.values()) - min(chars.values())


def part1(data):
    return solve(data, 10)


def part2(data):
    return solve(data, 40)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
