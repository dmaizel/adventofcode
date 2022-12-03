def read_file():
    with open("input.txt") as f:
        return f.read().strip()


def get_binary_string(hexaString):
    return bin(int('1'+hexaString, 16))[3:]


data = read_file()
print(data)
packet = get_binary_string(data)


def part1(start_bit):
    i = start_bit
    versions_total = int(packet[i : i + 3], 2)
    type_id = int(packet[i + 3 : i + 6], 2)
    i += 6

    if type_id == 4:  # literal value
        while True:
            i += 5
            if packet[i - 5] == "0":  # last value packet
                break
    else:
        if packet[i] == "0":
            endi = i + 16 + int(packet[i + 1 : i + 16], 2)
            i += 16
            while i < endi:
                i, version = part1(i)
                versions_total += version
        else:
            num_packets = int(packet[i + 1 : i + 12], 2)
            i += 12
            for _ in range(num_packets):
                i, version = part1(i)
                versions_total += version

    return i, versions_total


print("Total of version numbers:", part1(0)[1])
