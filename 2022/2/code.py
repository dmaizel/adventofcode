win_table = {
    'A': {
        'X': 4,
        'Y': 8,
        'Z': 3,
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9,
    },
    'C': {
        'X': 7,
        'Y': 2,
        'Z': 6,
    },
}

def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")

def part1(data):
    score = 0
    for r in data:
        opp, me = r.split(' ')
        score += win_table[opp][me]
    return score

def part2(data):
    score = 0
    for r in data:
        opp, pred = r.split(' ')
        sorted_outcomes = sorted(win_table[opp].values())
        if pred == 'X':
            score += sorted_outcomes[0]
        elif pred == 'Y':
            score += sorted_outcomes[1]
        else:
            score += sorted_outcomes[2]

    return score


if __name__ == "__main__":
    rounds = read_file()
    print(part1(rounds))
    print(part2(rounds))
