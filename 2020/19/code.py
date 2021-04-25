import re

def read_file():
    with open('input.txt') as f:
        return [x.split('\n') for x in f.read().strip().split('\n\n')]

def parse_rules(rules):
    rules_dict = {}
    for rule in rules:
        rule_num, val = rule.split(': ')
        rules_dict[int(rule_num)] = [x.split() for x in val.strip('"').split(' | ')]

    return rules_dict

def gen_regex(rules, rule_num=0, depth=15):
    if depth == 0:
        return ""
    rule = rules[rule_num][0][0]
    if any(char.isdigit() for char in rule):
        return "(" + '|'.join(["".join([gen_regex(rules, int(sub), depth-1) for sub in subrule]) for subrule in rules[rule_num]]) + ')'
    return rule

def part1(rules, messages):
    m = re.compile(gen_regex(parsed_rules))
    res = [m.fullmatch(message) for message in messages]
    return len([x for x in res if x])

def part2(rules, messages):
    rules[8] = [['42'], ['42', '8']]
    rules[11] = [['42', '31'], ['42', '11', '31']]

    m = re.compile(gen_regex(parsed_rules))
    res = [m.fullmatch(message) for message in messages]
    return len([x for x in res if x])

if __name__ == '__main__':
    rules, messages = read_file()
    parsed_rules = parse_rules(rules)
    print(part1(parsed_rules, messages))
    print(part2(parsed_rules, messages))
