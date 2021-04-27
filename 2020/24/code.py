from functools import lru_cache, wraps

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
    tiles_dict = {}

    for tile in tiles:
        cur = [0, 0]
        i = 0
        while i in range(len(tile)):
            if i+1 < len(tile) and str(tile[i: i+2]) in dir_trans:
                d = str(tile[i: i+2])
                i += 2
            else:
                d = tile[i]
                i += 1
            cur = [a+b for a, b in zip(cur, dir_trans[d])]

        if str(cur) not in tiles_dict:
            tiles_dict[str(cur)] = True
        else:
            tiles_dict[str(cur)] = not tiles_dict[str(cur)]

    return len([x for x in tiles_dict.values() if x]), tiles_dict

#@lru_cache()
def get_num_of_black_adj_tiles(tile, tiles_dict):
    neighbors = get_neighbors(tile, tiles_dict)
    return len([x for x in neighbors if x in tiles_dict and tiles_dict[x] == True])

def get_neighbors(tile, tiles_dict):
    adj = []
    tile = eval(tile)
    for d in dir_trans.values():
        adj.append([a+b for a,b in zip(tile, d)])

    return [str(x) for x in adj]

def solve(num_days, tiles_dict):
    for _ in range(num_days):
        new_tiles_dict = tiles_dict.copy()
        for tile, black in tiles_dict.items():
            num_black_adj = get_num_of_black_adj_tiles(tile, tiles_dict)
            if black and (num_black_adj == 0 or num_black_adj > 2):
                new_tiles_dict[tile] = False
            if not black and num_black_adj == 2:
                new_tiles_dict[tile] = True

            for n in get_neighbors(tile, tiles_dict):
                if n in tiles_dict:
                    continue
                num_black_adj = get_num_of_black_adj_tiles(n, tiles_dict)
                black = n in tiles_dict and tiles_dict[n]
                if black and (num_black_adj == 0 or num_black_adj > 2):
                    new_tiles_dict[n] = False
                if not black and num_black_adj == 2:
                    new_tiles_dict[n] = True

        tiles_dict = new_tiles_dict

    return len([x for x in tiles_dict.values() if x]) 
            
def part2(black_tiles):
    return solve(100, black_tiles)

if __name__ == '__main__':
    tiles = read_file()
    res1, tiles_dict = part1(tiles)
    print(res1)
    res2 = part2(tiles_dict)
    print(res2)
