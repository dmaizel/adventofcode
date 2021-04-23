import re

def readFile():
    with open("input.txt", "r") as f:
        return f.read().split('\n\n')

def prepare_dict(data):
    rules_regex = r'([\s\w]+): (\d+-\d+) or (\d+-\d+)'
    dic = {'rules': {}}
    for line in data[0].split('\n'):
        m = re.search(rules_regex, line)
        rule = m.group(1)
        valid_1 = m.group(2)
        valid_2 = m.group(3)
        dic['rules'][rule] = [tuple(valid_1.split('-')), tuple(valid_2.split('-'))]

    dic['your ticket'] = data[1].split(':\n')[1].split(',') 
    dic['nearby tickets'] = [x.split(',') for x in data[2].split(':\n')[1].split('\n')[:-1]]

    return dic

def inclusive_range(x, y):
    return [*range(x, y+1)]

def is_in_range(num, rules):
    return any([int(rule[0]) <= num <= int(rule[1]) for rule in rules])

def part1(data_dict):
    nearby_tickets = data_dict['nearby tickets']
    rules = data_dict['rules']
    error_rate = 0
    valid_ranges = []
    invalid_indexes = []

    for rule in data_dict['rules']:
        ranges = [r for r in data_dict['rules'][rule]]
        valid_ranges += ranges

    for index, ticket in enumerate(nearby_tickets):
        lists = [*(inclusive_range(*([int(num) for num in r])) for r in valid_ranges)]
        combined = [item for sublist in lists for item in sublist]
        for number in ticket:
            number = int(number)
            if number not in combined:
                error_rate += number
                invalid_indexes.append(index)

    return error_rate, invalid_indexes

def part2(data_dict, invalid_indexes):
    nearby_tickets = data_dict['nearby tickets']
    your_ticket = data_dict['your ticket']
    rules = data_dict['rules']
    error_rate = 0
    valid_tickets = []

    for i, _ in enumerate(nearby_tickets):
        if i not in invalid_indexes:
            valid_tickets.append(nearby_tickets[i])

    rule_to_pos_dict = {}

    for rule in data_dict['rules']:
        rule_range = data_dict['rules'][rule] 
        for i in range(len(data_dict['rules'])):
            if all(is_in_range(int(ticket[i]), rule_range) for ticket in valid_tickets):
                if rule not in rule_to_pos_dict:
                    rule_to_pos_dict[rule] = []
                else:
                    rule_to_pos_dict[rule].append(i)

    res = 1
    occ = {}
    new_role_to_pos = {}
    for rule in data_dict['rules']:
        num_list = rule_to_pos_dict[rule]
        for num in num_list:
            if num in occ:
                occ[num].append(rule)
            else:
                occ[num] = [rule]

    sorted_occ = dict(sorted(occ.items(), key=lambda item: len(item[1])))

    for k, v in sorted_occ.items():
        if v:
            rule = v[0]
            new_role_to_pos[rule] = k
            for ki, vi in sorted_occ.items():
                if rule in vi:
                    vi.remove(rule)

    for n in [v for k,v in new_role_to_pos.items() if k.startswith('departure')]:
        res *= int(your_ticket[n])

    return res
        
if __name__ == '__main__':
    data = readFile()
    data_dict = prepare_dict(data)
    res1, invalid_indexes = part1(data_dict)
    print(res1)
    res2 = part2(data_dict, invalid_indexes)
    print(res2)

