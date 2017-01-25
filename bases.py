#!python

import string
import math


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    return int(str_num, base)


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    result = num
    ret_num = []

    while result != 0:
        remainder = (math.modf((result / float(base)))[0]) * base
        result = result / base

        if remainder >= 10:
            ret_num.append(chr(97 + int(remainder - 10)))
        else:
            ret_num.append(str(int(remainder)))

    return "".join(ret_num[::-1])
    assert 2 <= base <= 36
    # TODO: Encode number


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """

    return encode(decode(str_num, base1), base2)
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    print(convert('3243', 16, 2))
