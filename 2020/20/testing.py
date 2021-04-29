def print_tile(tile):
    for row in tile:
        print(row)
    print('\n')

def flip_90(tile):
    new_tile = []
    size = len(tile)
    for row in range(size):
        s = []
        for column in range(size):
            s.append(tile[size - 1 - column][row])
        new_tile.append(s)
    return new_tile

def flip_v(tile):
    return [row[::-1] for row in tile]

tile = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print_tile(tile)
rotated = flip_90(tile)
print_tile(rotated)
flipped = flip_v(tile)
print_tile(flipped)



