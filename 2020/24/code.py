'''
east(e) -> (1, 0)
southeast(se) -> (1, -1)
southwest(sw) -> (-1, -1)
west(w) -> (-1, 0)
northwest(nw) -> (-1, 1)
northeast(ne) -> (1, 1)
'''

def read_file():
    with open('input.txt', 'r') as f:
        return f.read().strip().split('\n')

dir_trans = {
    'w': (-2, 0),
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'nw': (-1, 1),
    'ne': (1, 1)
}

def part1(tiles):
    black_tiles = set()

    for tile in tiles:
        cur = (0, 0)
        i = 0
        while i in range(len(tile)):
            if i+1 < len(tile) and str(tile[i: i+2]) in dir_trans:
                d = str(tile[i: i+2])
                i += 2
            else:
                d = tile[i]
                i += 1
            cur = tuple([a+b for a, b in zip(cur, dir_trans[d])])

        if cur not in black_tiles:
            black_tiles.add(cur)
        else:
            black_tiles.remove(cur)

    return len(black_tiles), black_tiles

def get_num_of_black_adj_tiles(tile, black_tiles):
    neighbors = get_neighbors(tile, black_tiles)
    return len([x for x in neighbors if x in black_tiles])

def get_neighbors(tile, black_tiles):
    return [tuple(x) for x in [[a+b for a,b in zip(tile, d)] for d in dir_trans.values()]]

def solve(num_days, black_tiles):
    for _ in range(num_days):
        new_tiles = set()
        to_check = set()

        for tile in black_tiles:
            to_check.add(tile)
            for n in get_neighbors(tile, black_tiles):
                to_check.add(n)

        for tile in to_check:
            num_black_adj = get_num_of_black_adj_tiles(tile, black_tiles)
            if (tile in black_tiles and 0 < num_black_adj <= 2) or (
                tile not in black_tiles and num_black_adj == 2
            ):
                new_tiles.add(tile)
        black_tiles = new_tiles

    return len(black_tiles) 
            
def part2(black_tiles):
    return solve(100, black_tiles)

if __name__ == '__main__':
    tiles = read_file()
    res1, black_tiles = part1(tiles)
    print(res1)
    res2 = part2(black_tiles)
    print(res2)
