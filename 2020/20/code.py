def read_file():
    tiles = {}

    with open('input.txt') as f:
        for x in f.read().strip().split('\n\n'):
            tn, t = x.strip('Tile ').split(':')
            tiles[int(tn)] = {
                                'grid': t.strip().split('\n'),
                                'sides': [],
                                'neighbors': {}    
                            }

    return tiles

def rotate_tile(tile):
    # Rotate a tile clockwise
    res = list(zip(*tile[::-1]))
    res = [''.join(x) for x in [list(x) for x in res]]
    
    return res

def update_sides(tiles):
    for k, v in tiles.items():
        grid = v['grid']
        sides = [grid[0], grid[-1], ''.join([g[0] for g in grid]), ''.join([g[-1] for g in grid])]
        sides += [s[::-1] for s in sides]
        v['sides'] = sides

    return tiles

def part1(tiles):
    for k, v in tiles.items():
        for ki, vi in tiles.items():
            if k == ki:
                continue
            shared = [side for side in vi['sides'] if side in v['sides']]
            for s in shared:
                v['neighbors'][ki] = s
                vi['neighbors'][k] = s

    corners = [t for t in tiles if len(tiles[t]['neighbors']) == 2]

    res = 1
    for c in corners:
        res *= c

    return res

if __name__ == '__main__':
    tiles = read_file()
#    for k, value in tiles.items():
#        tile = value['grid']
#        break
#    for line in tile:
#        print(line)
#
#
#    print('=================')
#    tile = rotate_tile(tile)
#
#    for line in tile:
#        print(line)
    tiles = update_sides(tiles)
    print(part1(tiles))
