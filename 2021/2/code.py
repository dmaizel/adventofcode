def read_file():
    with open('input.txt') as f:
        return [tuple(x.split(' ')) for x in f.read().strip().split('\n')]

def add_to_dir1(pos, dir, num):
    if dir == "forward":
        pos[0] += num
    elif dir == "up":
        pos[1] -= num
    elif dir == 'down':
        pos[1] += num

    return pos


def add_to_dir2(pos, dir, num, aim):
    if dir == "forward":
        pos[0] += num
        pos[1] += aim * num
    elif dir == "up":
        aim -= num
    elif dir == 'down':
        aim += num

    return pos, aim

def part1(data):
    curr_position = [0, 0]
    for line in data:
        dir, num = line
        curr_position = add_to_dir1(curr_position, dir, int(num))
    return curr_position[0] * curr_position[1]

def part2(data):
    aim = 0
    curr_position = [0, 0]
    for line in data:
        dir, num = line
        curr_position, aim = add_to_dir2(curr_position, dir, int(num), aim)
    return curr_position[0] * curr_position[1]

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))
