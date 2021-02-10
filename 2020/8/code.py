def readFile():
    return open('input.txt').read().splitlines()

def parse_data(data):
    instructions = {}

    for index, line in enumerate(data):
        op, arg = line.split(' ')
        instructions[index] = [op, eval(arg)]
    
    return instructions

def run(instructions):
    acc = 0
    pointer = 0
    visited = []
    size = len(instructions)

    while pointer not in visited and pointer != size:
        visited.append(pointer)
        op, arg = instructions[pointer]
        
        if op== 'acc':
            acc += arg
            pointer += 1
        elif op== 'jmp':
            pointer += arg
        else:
            pointer += 1
    return pointer, acc
    

def part1(instructions):
   return run(instructions)[1] 

def part2(instructions):
    size = len(instructions)
    for i in range(size):
        op, arg = instructions[i]
        if op== 'jmp':
            instructions[i][0] = 'nop'
            pointer, acc = run(instructions)
            instructions[i][0] = 'jmp'
        elif op== 'nop':
            instructions[i][0] = 'jmp'
            pointer, acc = run(instructions)
            instructions[i][0] = 'nop'
        else:
            continue
    
        if pointer == size:
            return acc


if __name__ == '__main__':
    instructions = parse_data(readFile())
    print(part1(instructions))
    print(part2(instructions))
