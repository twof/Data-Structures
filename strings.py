#!python

import string
import re


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    if text == '':
        return True

    p = re.compile('[^a-zA-Z]')
    text = p.sub('', text)

    left = 0
    right = len(text) - 1

    is_different_case = ord(text[left])\
        in [ord(text[right]) - 32, ord(text[right]) + 32]\
        or ord(text[right]) in [ord(text[left]) - 32, ord(text[left]) + 32]
    is_same_case = text[left] == text[right]

    while left < right:
        if not is_different_case and not is_same_case:
            return False
        else:
            left += 1
            right -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    if text == '' or left > right:
        return True

    if left is None:
        p = re.compile('[^a-zA-Z]')
        text = p.sub('', text)

        left = 0
        right = len(text) - 1

    is_different_case = ord(text[left])\
        in [ord(text[right]) - 32, ord(text[right]) + 32]\
        or ord(text[right]) in [ord(text[left]) - 32, ord(text[left]) + 32]
    is_same_case = text[left] == text[right]

    if not is_different_case and not is_same_case:
        return False
    else:
        return is_palindrome_recursive(text, left + 1, right - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    print(is_palindrome_recursive('A'))
