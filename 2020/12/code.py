def readFile():
    return open('input.txt').read().split()

directions = ['N', 'E', 'S', 'W']

def move(x, y, value, direction):
    if direction == 'N':
        y += value
    elif direction == 'S':
        y -= value
    elif direction == 'E':
        x += value
    elif direction == 'W':
        x -= value
    
    return x, y
    

def rotate(direction, degrees, current_dir):
    if direction == 'R' or direction == 'L':
        num = degrees / 90
        current_dir = directions[int(((directions.index(current_dir) + num if direction == 'R' else directions.index(current_dir) - num)) % 4 )]

    return current_dir
        

def part1(instructions):
    current_dir = 'E'
    x, y = 0, 0 
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        
        if action == 'F':
            action = current_dir        

        current_dir = rotate(action, value, current_dir)
        x, y = move(x, y, value, action)    

    return abs(x) + abs(y)
               

def part2(instructions):
    wx, wy = 10, 1 
    x, y = 0, 0
    
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        
        if action == 'F':
            for i in range(value):
                x += wx
                y += wy
        elif action == 'R':
            value //= 90
            for i in range(value):
                wx, wy = wy, -wx
        elif action == 'L': 
            value //= 90
            for i in range(value):
                wx, wy = -wy, wx
        else:    
            wx, wy = move(wx, wy, value, action)    

    return abs(x) + abs(y)
        
    

if __name__ == '__main__':
    instructions = readFile()
    print(part1(instructions))
    print(part2(instructions))
