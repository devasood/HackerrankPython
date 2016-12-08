def get_int():
    return int(get_string())


def get_float():
    return float(get_string())


def get_ints():
    return [int(x) for x in input().split()]


def get_string():
    return input()
