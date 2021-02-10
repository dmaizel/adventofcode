def readFile():
    with open('input.txt') as f:
        arrival_time, values = f.read().split()
        arrival_time = int(arrival_time)
        values = str(values).strip().split(',')
        bus_ids = [{"value": int(values[i]), "index": i}
                    for i in range(len(values))
                    if values[i] != 'x']
        return arrival_time, bus_ids

def part1(arrival_time, bus_ids):
    bus_ids = [bus_id['value'] for bus_id in bus_ids]
    dic = {i: i - arrival_time%i for i in bus_ids}
    key_min = min(dic.keys(), key=(lambda k: dic[k]))

    return key_min * dic[key_min]

def part2(bus_ids):
    time = step = 1
    for bus in bus_ids:
        while(time + bus['index']) % bus['value'] != 0:
            time += step
        step *= bus['value']
    return time

if __name__ == '__main__':
    arrival_time, bus_ids = readFile()
    print(part1(arrival_time, bus_ids))
    print(part2(bus_ids))

