def read_file():
    with open('input.txt') as f:
        return list(map(int, f.read().strip().split(',')))

def part1(data, noun, verb):
    data = data.copy()
    data[1] = noun
    data[2] = verb
    op_code_index = 0

    while True:
        if data[op_code_index] == 99:
            return data[0]

        first = data[data[op_code_index+1]]
        second = data[data[op_code_index+2]]

        if data[op_code_index] == 1:
            res = first + second
        elif data[op_code_index] == 2:
            res = first * second
        else:
            raise Exception('Wrong op code - something went wrong')

        data[data[op_code_index+3]] = res
        op_code_index += 4

def part2(data):
    for noun in range(100):
        for verb in range(100):
            if part1(data, noun, verb) == 19690720:
                return 100 * noun + verb

data = read_file()
print(part1(data, 12, 2))
print(part2(data))
