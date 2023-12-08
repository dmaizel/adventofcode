def read_file():
    with open("input.txt") as f:
        return f.read().strip().splitlines()


if __name__ == "__main__":
    data = read_file()
    print(data)
