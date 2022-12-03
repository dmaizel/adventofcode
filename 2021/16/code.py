def read_file():
    with open("test_input.txt") as f:
        return f.read().strip()


def get_binary_string(hexaString):
    return bin(int(hexaString, 16))[2:]


def get_version(packet):
    return int(packet[0:3], 2)


def get_packet_type_id(packet):
    return int(packet[3:6], 2)


def is_literal_value(packet_type_id):
    return packet_type_id == 4


def get_literal_value(packet):
    curr_idx = 6
    res = ""

    while int(packet[curr_idx]) == 1:
        print('here')
        res += packet[curr_idx + 1 : curr_idx + 5]
        curr_idx += 5

    res += packet[curr_idx + 1: curr_idx + 5]

    return res


def part1(data):
    packet = get_binary_string(data)
    version = int(get_version(packet))
    packet_type_id = get_packet_type_id(packet)
    literal_value = get_literal_value(packet)
    print(version)
    print(packet_type_id)
    print(literal_value)


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
