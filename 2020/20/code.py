import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Tile:
    def __init__(self, tile, tile_id):
        self.tile = tile
        self.id = int(tile_id)
        self.edge_len = len(tile)

    def can_below(self, another_tile):
        #if self.id == another_tile.id:
        #    return False
        cond = self.tile[-1] == another_tile.tile[0]
        #print(f'tile {another_tile.id} {"can" if cond else "cannot"} be below tile {self.id}')
        return cond

    def can_right(self, another_tile):
        #if self.id == another_tile.id:
        #    return False
        cond = [x[0] for x in another_tile.tile] == [x[-1] for x in self.tile]
        #print(f'tile {another_tile.id} {"can" if cond else "cannot"} be right to tile {self.id}')
        return cond

    def flip(self):
        res = [''.join(reversed(row)) for row in self.tile]
        self.tile = res

    def rotate_right(self):
        new_tile = []
        size = len(self.tile)
        for row in range(size):
            s = []
            for column in range(size):
                s.append(self.tile[size - 1 - column][row])
            new_tile.append(''.join(s))

        self.tile = new_tile

    def rotations(self):
        rotations = []
        for _ in range(2):
            for _ in range(4):
                rotations.append(Tile(self.tile, self.id))
                self.rotate_right()
            self.flip()

        return rotations

    def remove_border(self):
        return [row[1:-1] for row in self.tile[1:-1]]

    def print(self):
        print('tile_id: ', self.id)
        for row in self.tile:
            print(row)

def print_row(tile_row):
    for j in range(tile_row[0].edge_len):
        for tile in tile_row:
            print(tile.tile[j], end='  ')
        print('')
    print('')

def print_grid(tile_grid):
    for row in tile_grid:
        print_row(row)

def print_grid_numbers(tile_grid):
    for row in tile_grid:
        for tile in row:
            print(tile.id, end=' ')
        print('')

def rotate_grid_right(grid):
    new_grid = []
    size = len(grid)
    for row in range(size):
        s = []
        for column in range(size):
            s.append(grid[size - 1 - column][row])
        new_grid.append(s)

    return new_grid

def flip_grid(grid):
    new_grid = grid[::-1]

    return new_grid

def build_final_grid(temp_grid):
    t_grid = temp_grid
    res = []

    for row in t_grid:
        for i in range(row[0].edge_len-2):
            row_str = ''
            for tile in row:
                row_str += tile.remove_border()[i]
            res.append(row_str)

    return res

def grid_rotations(grid):
    rotations = []
    new_grid = grid.copy()
    for _ in range(2):
        for _ in range(4):
            rotations.append(new_grid)
            new_grid = rotate_grid_right(new_grid)
        new_grid = flip_grid(new_grid)

    return rotations

#def pattern_rotations(pattern):
#    res = []
#    p = pattern
#    for _ in range(4):
#        res.append(p)
#        p = rotate_grid_right(p)
#
#    return res
#
#def grid_rotations(pattern):
#    patterns = [pattern]
#    new_patterns = []
#    
#    horizontal = pattern[::-1]
#    vertical = [row[::-1] for row in pattern if row]
#    both = [row[::-1] for row in pattern[::-1] if row]
#
#    flipped_patterns =  [horizontal] + [vertical] + [both]
#    for pattern in flipped_patterns:
#        new_patterns.extend(pattern_rotations(pattern))
#        new_patterns.extend([pattern])
#
#    for pattern in new_patterns:
#        if pattern not in patterns:
#            patterns.append(pattern)
#
#    return patterns



def read_file():
    tiles = []

    with open('input.txt') as f:
        for x in f.read().strip().split('\n\n'):
            tile_id, tile = x.strip('Tile ').split(':')
            tiles.append(Tile(tile.strip().split('\n'), tile_id))
    
    return tiles

tiles = read_file()
grid_size = int(len(tiles) ** 0.5)
grid = [[[] for i in range(grid_size)] for _ in range(grid_size)]

monster_offsets = [
    (0, 18),
    (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
    (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
]
monster_width = 20
monster_height = 3

def search(tiles, row, col, visited):
    if row == grid_size:
        print('Finished!')
        return grid[0][0].id * grid[-1][0].id * grid[0][-1].id * grid[-1][-1].id

    for tile in tiles:
        if tile.id not in visited:
            if row > 0 and not grid[row-1][col].can_below(tile):
                continue
            if col > 0 and not grid[row][col-1].can_right(tile):
                continue
            grid[row][col] = tile
            visited.add(tile.id)
            if col == grid_size - 1:
                res = search(tiles, row + 1, 0, visited)
            else:
                res = search(tiles, row, col + 1, visited)
            if res is not None:
                return res
            visited.remove(tile.id)

    return None

def part1(tiles):
    tiles_to_check = []
    for tile in tiles:
        tiles_to_check.extend(tile.rotations())

    visited = set()
    res = search(tiles_to_check, 0, 0, visited)
    return res

def print_image(image):
    for row in image:
        print(row)

def part2(my_grid):
    my_rotations = grid_rotations(my_grid)
        
    for g in my_rotations:
        image = build_final_grid(g)
        #print_image(image)
        #print('====================================================')
        #monsters = count_monsters(image)
        hashes = sum(sum(1 for c in row if c == '#') for row in image)
        if monsters > 0:
            print('got it')
            return hashes - monsters * len(monster_offsets)

def has_monster(image, x, y):
    for offset in monster_offsets:
        sx = x + offset[0]
        sy = y + offset[1]
        if image[sx][sy] != '#':
            #print('checking ', (sx, sy))
            return False

    return True

def count_monsters(image):
    'Return the total number of sea monsters in the image'
    count = 0
    assert len(image) == len(image[0])
    for x in range(len(image) - monster_height):
        for y in range(len(image[0]) - monster_width):
            if has_monster(image, x, y):
                count += 1
    return count

if __name__ == '__main__':
    print(part1(tiles))
    #print(part2(grid))
    print_grid(grid)
    #r = grid_rotations(grid)
    #for i in r:
    #    image = build_final_grid(i)
    #    print_image(image)
        #print_grid_numbers(i)
     #   print('')
    #print_grid_numbers(grid)
    #print()
    #print_grid_numbers(flip_grid(grid))
