def readFile():
    with open('input.txt') as f:
        return [line.strip().split(' = ') for line in f.readlines()]

def part1(input):
    mask_and = mask_or = None
    memory = dict()

    for instruction in input:
        if instruction[0] == 'mask':
            mask_and = int(instruction[1].replace("X", "1"), 2)
            mask_or = int(instruction[1].replace("X", "0"), 2)
        else:
            index = int(instruction[0][4:-1])
            value = (int(instruction[1]) & mask_and) | mask_or
            memory[index] = value
    return sum(memory.values())

def generate_masks(mask):
    masks = []
    num_x = len([x for x in mask if x == 'X'])
    x_replacements = []

    for i in range(2**num_x):
        bin_str = "{0:b}".format(i)
        if len(bin_str) != num_x:
            bin_str = '0'*(num_x - len(bin_str)) + bin_str
        x_replacements.append(bin_str)

    for x_replacement in x_replacements:
        temp_mask = mask
        j = 0
        for index, ch in enumerate(temp_mask):
            if ch == 'X':
                s = list(temp_mask)
                s[index] = list(x_replacement)[j]
                temp_mask = ''.join(s)
                j+=1
        masks.append(temp_mask)

    return masks




def part2(input):
    memory = dict()

    for instruction in input:
        if instruction[0] == 'mask':
            current_mask = instruction[1]
        else:
            address = bin(int(instruction[0][4:-1])).split('0b')[1]
            if len(address) != 36:
                 address = '0'*(36-len(address)) + address
            value = int(instruction[1])

            for mask in generate_masks(current_mask):
                temp_addr_list = list(address)
                for index, char in enumerate(mask):
                    if 'X' == list(current_mask)[index]:
                        temp_addr_list[index] = char
                    elif list(current_mask)[index] == '1':
                        temp_addr_list[index] = '1'
                memory[int(''.join(temp_addr_list), 2)] = value

    return sum(memory.values())


if __name__ == '__main__':
    input = readFile()
    #print(part1(input))
    print(part2(input))

