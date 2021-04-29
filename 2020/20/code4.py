from random import randint
import sys
colors = {
    'HEADER' : '\033[95m',
    'OKBLUE' : '\033[94m',
    'OKCYAN' : '\033[96m',
    'OKGREEN' : '\033[92m',
    'WARNING' : '\033[93m',
    'FAIL' : '\033[91m'
}

last_color = None

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
        #res = [''.join(row[::-1]) for row in self.tile]
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
        #print('Before:')
        #self.print()
        self.tile = [row[1:-1] for row in self.tile[1:-1]]
        #print('After:')
        #self.print()

    def print(self):
        print('tile_id: ', self.id)
        for row in self.tile:
            print(row)

def print_row(tile_row, color):
    for j in range(tile_row[0].edge_len):
        for tile in tile_row:
            print(f'{color}{tile.tile[j]}', end='  ')
        print('')
    print('')

def print_grid(tile_grid):
    stop = len(colors.keys()) - 1
    idx = randint(0, stop)
    global last_color
    color = ''
    while color == last_color:
        color = list(colors.values())[idx]
    last_color = color
    #print(idx)
    #color = colors[colors.keys()[randint(0, len(colors.keys())-1)]]
    for row in tile_grid:
        print_row(row, color)

def print_grid_numbers(tile_grid):
    for row in tile_grid:
        for tile in row:
            print(tile.id, end=' ')
        print('')

def rotate_tile_right(tile):
    new_tile = Tile(tile.tile, tile.id)
    new_tile.rotate_right()
    return new_tile

def flip_tile(tile):
    new_tile = Tile(tile.tile, tile.id)
    new_tile.flip()
    return new_tile

def rotate_grid_right(grid):
    new_grid = []
    size = len(grid)
    for row in range(size):
        s = []
        for column in range(size):
            s.append(rotate_tile_right(grid[size - 1 - column][row]))
        new_grid.append(s)

    return new_grid

def rotate_grid_right1(grid, num_times):
    new_grid = []
    size = len(grid)
    ret = None
    for i in range(num_times):
        if ret is not None:
            new_grid = ret
        for row in range(size):
            s = []
            for column in range(size):
                s.append(rotate_tile_right(grid[size - 1 - column][row], num_times))
            new_grid.append(s)
        ret = new_grid

    return ret

def flip_grid(grid):
    new_grid = grid.copy()
    res = new_grid.copy()
    #new_grid = grid[::-1]
    #print('Before')
    #print_grid(new_grid)
    new_grid = [row[::-1] for row in new_grid]
    for index, row in enumerate(new_grid):
        res[index] = []
        for tile in row:
            res[index].append(flip_tile(tile))

    #print('After')
    #print_grid(new_grid)

    return res

def build_final_grid(temp_grid):
    t_grid = temp_grid
    res = []

    for row in t_grid:
        for i in range(8):
            row_str = ''
            for tile in row:
                row_str += tile.tile[i]
            res.append(row_str)

    return res

def grid_rotations1(grid):
    rotations = []
    new_grid = grid.copy()
    for _ in range(2):
        for _ in range(4):
            rotations.append(new_grid)
            new_grid = rotate_grid(new_grid)
        new_grid = flip_grid(new_grid)

    return rotations

def rotate_grid(g):
    return rotate_grid_right(g)

def grid_rotations(grid):
    rotations = []
    new_grid = grid.copy()

    rotations.append(new_grid.copy())
    rotations.append(rotate_grid_right(new_grid.copy()))
    rotations.append(rotate_grid_right(rotate_grid_right(new_grid.copy())))
    rotations.append(rotate_grid_right(rotate_grid_right(rotate_grid_right(new_grid.copy()))))
    rotations.append(flip_grid(new_grid.copy()))
    rotations.append(rotate_grid_right(flip_grid(new_grid.copy())))
    rotations.append(rotate_grid_right(rotate_grid_right(flip_grid(new_grid.copy()))))
    rotations.append(rotate_grid_right(rotate_grid_right(rotate_grid_right(flip_grid(new_grid.copy())))))

    return rotations

def read_file():
    tiles = []

    with open('input.txt') as f:
        for x in f.read().strip().split('\n\n'):
            tile_id, tile = x.strip('Tile ').split(':')
            tiles.append(Tile(tile.strip().split('\n'), tile_id))
    
    return tiles

tiles = read_file()
grid_size = int(len(tiles) ** 0.5)

monster_offsets = [
    (0, 18),
    (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
    (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
]
monster_width = 20
monster_height = 3

def search(tiles, row, col, visited, grid):
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
                res = search(tiles, row + 1, 0, visited, grid)
            else:
                res = search(tiles, row, col + 1, visited, grid)
            if res is not None:
                return res
            visited.remove(tile.id)

    return None

def part1(tiles):
    tiles_to_check = []
    for tile in tiles:
        tiles_to_check.extend(tile.rotations())

    visited = set()
    grid = [[[] for i in range(grid_size)] for _ in range(grid_size)]
    res = search(tiles_to_check, 0, 0, visited, grid)
    return res, grid

def print_image(image):
    for row in image:
        print(row)

def part2(my_grid):
    for row in my_grid:
        for tile in row:
            tile.remove_border()

    my_rotations = grid_rotations(my_grid)

    for g in my_rotations:
        image = build_final_grid(g)
        #print_image(image)
        #print('====================================================')
        monsters = count_monsters(image)
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
    res1, grid = part1(tiles)
    print(res1)
    test_image = [line.strip('\n') for line in open('test_image.txt').read().strip().split('\n')]
    print_image(test_image)
    print('\n')
    #print_grid(grid)
    #g = grid_rotations(grid)
    #for g in r:
    #    print_grid(g)
    #print_grid(g[0])
    #print_grid(g[1])
    #print_grid(g[2])
    #print_grid(g[3])
    #print_grid(g[4])
    #print_grid(g[5])
    #print_grid(g[6])
    #print_grid(g[7])
    #for row in grid:
    #    for tile in row:
    #        tile.remove_border()
    #print_grid(g)
    
    #for row in grid:
    #    for tile in row:
    #        tile.remove_border()
    #r = grid_rotations(grid)
    #image = build_final_grid(r[7])
    #print_image(image)
    #for i in r:
    #    image = build_final_grid(i)
    #    print_image(image)
    #    print()
    #    print(image == test_image)
        #print_image(image)
    print(part2(grid))
    
    #print_grid(grid)
    #r = grid_rotations(grid)
    #for i in r:
    #    image = build_final_grid(i)
    #    print_image(image)
        #print_grid_numbers(i)
     #   print('')
    #print_grid_numbers(grid)
    #print()
    #print_grid_numbers(flip_grid(grid))
