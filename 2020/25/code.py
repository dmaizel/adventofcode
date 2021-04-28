def read_file():
    with open('input.txt', 'r') as f:
        return [int(x) for x in f.read().strip().split('\n')]

def get_loop_size(pk, subject_num):
    val = 1
    loop_size = 0

    while val != pk:
        loop_size += 1  
        val *= subject_num
        val %= 20201227

    return loop_size

def transform(subject_num, loop_size):
    val = 1

    for _ in range(loop_size):
        val *= subject_num
        val %= 20201227

    return val

def part1(card_pk, door_pk):
    card_loop_size = get_loop_size(card_pk, 7)
    #door_loop_size = get_loop_size(door_pk, 7)
    enc_key = transform(door_pk, card_loop_size)

    return enc_key

if __name__ == '__main__':
    card_pk, door_pk = read_file()
    print(part1(card_pk, door_pk))

