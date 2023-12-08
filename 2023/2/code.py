import re

def read_file():
    with open('input.txt') as f:
        return f.read().splitlines()

def part1(data):
    games = {}
    for game in data:
        a, b = game.split(':')
        _, game_num = a.split()
        game_num = int(game_num)
        games[game_num] = {'blue': 0, 'green': 0, 'red': 0}
        for i in b.replace(';', ',').split(','):
            num, color = i.split()
            games[game_num][color.strip()] = max(games[game_num][color.strip()], int(num.strip()))

    possible = []
    for game in games:
        if games[game]['blue'] <= 14 and games[game]['green'] <= 13 and games[game]['red'] <= 12:
            possible.append(int(game))

    return sum(possible)

def part2(data):
    games = {}
    for game in data:
        a, b = game.split(':')
        _, game_num = a.split()
        game_num = int(game_num)
        games[game_num] = {'blue': 0, 'green': 0, 'red': 0}
        for i in b.replace(';', ',').split(','):
            num, color = i.split()
            games[game_num][color.strip()] = max(games[game_num][color.strip()], int(num.strip()))

    possible = []
    for game in games:
        possible.append(games[game]['blue'] * games[game]['green'] * games[game]['red'])

    return sum(possible)

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))
