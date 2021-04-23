import re

def readFile():
    with open("input.txt", "r") as f:
        return f.read().strip()

def prepare_data(raw_data):
    rules_raw, myticket_raw, others_raw = [x.split('\n') for x in raw_data.split('\n\n')]
    
    rules = {}
    for rule in rules_raw:
        match = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", rule)
        name = match.group(1)
        nums = list(map(int, match.groups()[1:]))
        rules[name] = nums

    others = [list(map(int, x.split(','))) for x in others_raw[1:]]
    myticket = list(map(int, myticket_raw[1].split(',')))

    return rules, others, myticket

def is_in_range(num, rules):
    return any([v[0] <= num <= v[1] or v[2] <= num <= v[3] for v in rules.values()])

def part1(rules, others):
    error_rate = 0
    valid_ranges = []
    invalid_indexes = []

    return sum([num for other in others for num in other if not is_in_range(num, rules)])

def part2(rules, others, myticket):
    valid_others = [other for other in others if all([is_in_range(num,rules) for num in other])]
    
    occurences = {}
    for name, ranges in rules.items():
        occurences[name] = [i for i in range(len(rules)) if all([is_in_range(l[i], {name: ranges}) for l in valid_others])]

    sorted_occurences = dict(sorted(occurences.items(), key=lambda item: len(item[1])))

    matches = {}

    for name, possibilities in sorted_occurences.items():
        index = [i for i in possibilities if i not in matches][0]
        matches[index] = name

    res = 1
    for index, value in enumerate(myticket):
        if 'departure' in matches[index]:
            res *= value
    
    return res

if __name__ == '__main__':
    raw_data = readFile()
    rules, others, myticket = prepare_data(raw_data)
    print(part1(rules, others))
    print(part2(rules, others, myticket))
