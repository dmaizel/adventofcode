from collections import defaultdict


def read_file():
    with open("input.txt") as f:
        return f.read().strip().split("\n")


def get_dir_sizes(data):
    dir_to_size = defaultdict(int)
    paths = []
    for line in data:
        words = line.strip().split()
        if words[0] == "$":
            if words[1] == "cd":
                path = words[2]
                if path == "..":
                    paths.pop()
                else:
                    paths.append(path)
            elif words[1] == "ls":
                continue
        else:
            try:
                size = int(words[0])
                for i in range(len(paths) + 1):
                    dir_to_size["/".join(paths[:i]).replace("//", "/")] += size
            except:
                pass

    return dir_to_size


def part1(data):
    dir_to_size = get_dir_sizes(data)
    ans = 0
    for v in dir_to_size.values():
        if v <= 100000:
            ans += v

    return ans


def part2(data):
    dir_to_size = get_dir_sizes(data)
    dic = {k: v for k, v in sorted(dir_to_size.items(), key=lambda item: item[1])}

    available = 70000000 - dic["/"]
    need_space = 30000000
    for v in dic.values():
        if available + v >= need_space:
            return v

    return -1


if __name__ == "__main__":
    data = read_file()
    print(part1(data))
    print(part2(data))
