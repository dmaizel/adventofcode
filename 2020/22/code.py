def read_file():
    with open('input.txt', 'r') as f:
        p1_raw, p2_raw = f.read().strip().split('\n\n')
        p1 = [int(num) for num in p1_raw.split('\n')[1:]]
        p2 = [int(num) for num in p2_raw.split('\n')[1:]]

    return p1, p2

def part1(p1, p2):
    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.extend([c1, c2])
        elif c1 < c2:
            p2.extend([c2, c1])

    d = p1 if p1 else p2

    return calc_score(d)

def game(p1, p2, is_first_game=False):
    records = {}

    while p1 and p2:
        key = str(p1) + str(p2)
        if key in records:
            return False
        records[key] = None
        
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if len(p1) >= c1 and len(p2) >= c2:
            winner_is_2 = game(p1[:c1], p2[:c2])
        else:
            winner_is_2 = c2 > c1

        if winner_is_2:
            p2.extend([c2, c1])
        else:
            p1.extend([c1, c2])

    if is_first_game:
        return p2 if winner_is_2 else p1

    return winner_is_2

def calc_score(deck):
    res = 0
    counter = 1
    while deck:
        res += deck.pop() * counter
        counter += 1

    return res

def part2(p1, p2):
    winning_deck = game(p1, p2, True)

    return calc_score(winning_deck)

if __name__ == '__main__':
    p1, p2 = read_file()
    print(part1(p1.copy(), p2.copy()))
    print(part2(p1, p2))
