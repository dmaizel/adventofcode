import re

def calc_dist(pos):
    x, y = pos
    return abs(x) + abs(y)

def get_wire_position(wire):
    x, y = 0, 0 
    curr_steps = 0
    positions = set()
    steps_to_pos = {}

    for i in range(len(wire)):
        for _ in range(int(wire[i][1:])):
            direction = wire[i][0]

            if   direction == "R":
                x +=1
            elif direction == "L":
                x -=1
            elif direction == "D":
                y +=1
            elif direction == "U":
                y -=1

            curr_steps += 1
            position = (x, y)

            positions.add(position)
            if position not in steps_to_pos:
                steps_to_pos[position] = curr_steps

    return positions, steps_to_pos


def read_file():
    with open('input.txt') as f:
        return [line.split(',') for line in f.read().strip().split('\n')]


def part1(wires):
    path1, _ = get_wire_position(wires[0])
    path2, _ = get_wire_position(wires[1])

    intersections = [x for x in path1 if x in path2]

    return min([calc_dist(x) for x in intersections])
    

def part2(wires):
    path1, steps_to_pos1 = get_wire_position(wires[0])
    path2, steps_to_pos2 = get_wire_position(wires[1])

    return min(steps_to_pos1[pos] + steps_to_pos2[pos] for pos in path1 if pos in path2)


wires = read_file()
print(part1(wires))
print(part2(wires))
