monster_offsets = [
    (0, 18),
    (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
    (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
]
monster_width = 20
monster_height = 3

def read_file():
    tiles = []

    with open('input.txt') as f:
        for x in f.read().strip().split('\n\n'):
            tile_id, tile = x.strip('Tile ').split(':')
            tiles.append(Tile(tile.strip().split('\n'), tile_id))
    
    return tiles

class Tile:
    def __init__(self, tile, tile_id):
        self.tile = tile
        self.id = int(tile_id)
        self.edge_len = len(tile)

    def can_below(self, another_tile):
        return self.tile[-1] == another_tile.tile[0]

    def can_right(self, another_tile):
        return [x[0] for x in another_tile.tile] == [x[-1] for x in self.tile]

    def flip(self):
        res = [''.join(row[::-1]) for row in self.tile]
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
        self.tile = [row[1:-1] for row in self.tile[1:-1]]

    #def print(self):
    #    print('tile_id: ', self.id)
    #    for row in self.tile:
    #        print(row)

#def print_row(tile_row, color):
#    for j in range(tile_row[0].edge_len):
#        for tile in tile_row:
#            print(tile.tile[j], end='  ')
#        print('')
#    print('')
#
#def print_grid(tile_grid):
#    for row in tile_grid:
#        print_row(row)
#
#def print_grid_numbers(tile_grid):
#    for row in tile_grid:
#        for tile in row:
#            print(tile.id, end=' ')
#        print('')

def build_image(grid):
    my_grid = grid.copy()
    res = []
    for row in my_grid:
        for tile in row:
            tile.remove_border()

    for row in my_grid:
        for i in range(row[0].edge_len-2):
            row_str = ''
            for tile in row:
                row_str += tile.tile[i]
            res.append(row_str)

    return res

def search(tiles, row, col, visited, grid):
    grid_size = len(grid)
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

def part1(tiles, grid_size):
    tiles_to_check = []
    for tile in tiles:
        tiles_to_check.extend(tile.rotations())

    visited = set()
    grid = [[[] for i in range(grid_size)] for _ in range(grid_size)]
    res = search(tiles_to_check, 0, 0, visited, grid)
    return res, grid

def rotate_image(image):
    new_image = []
    size = len(image)
    for row in range(size):
        s = []
        for column in range(size):
            s.append(image[size - 1 - column][row])
        new_image.append(s)

    return new_image

def image_rotations(image):
    rotations = []
    new_image = image.copy()
    for _ in range(2):
        for _ in range(4):
            rotations.append(new_image)
            new_image = rotate_image(new_image)
        new_image = flip_image(new_image)

    return rotations

def flip_image(image):
    return [row[::-1] for row in image]

#def print_image(image):
#    for row in image:
#        print(row)

def part2(my_grid):
    first_image = build_image(my_grid)

    for image in image_rotations(first_image):
        monsters = count_monsters(image)
        hashes = sum(sum(1 for c in row if c == '#') for row in image)
        if monsters > 0:
            return hashes - monsters * len(monster_offsets)

def has_monster(image, x, y):
    for offset in monster_offsets:
        sx = x + offset[0]
        sy = y + offset[1]
        if image[sx][sy] != '#':
            return False

    return True

def count_monsters(image):
    count = 0
    assert len(image) == len(image[0])
    for x in range(len(image) - monster_height):
        for y in range(len(image[0]) - monster_width):
            if has_monster(image, x, y):
                count += 1
    return count

if __name__ == '__main__':
    tiles = read_file()
    grid_size = int(len(tiles) ** 0.5)
    res1, grid = part1(tiles, grid_size)
    print(res1)
    print(part2(grid))
