def read_file():
    with open("test_input.txt") as f:
        trans = str.maketrans("[]", "()")
        return tuple(map(lambda line: eval(line.translate(trans)), f))


def is_number(p):
    return type(p) is int


def explode(pair, depth=0):
    if is_number(pair):
        return None, pair, None, False

    left, right = pair

    if depth == 4:
        return left, 0, right, True

    left_num, new_left, right_num, did_explode = explode(left, depth+1)
    # Check results
    # if did_explode == True then return, no more explosions.

    left_num, new_left, right_num, did_explode = explode(left, depth+1)
    # Check results
    # if did_explode == True then return, no more explosions.


    # None of the left and right parts exploded, just return the pair as is.
    return None, pair, None, False


def add_to_leftmost(pair, num):
    if is_number(pair):
        return pair + num

    left, right = pair
    reutrn (add_to_leftmost(left, num), right)

if __name__ == "__main__":
    data = read_file()
    print(data)
