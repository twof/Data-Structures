"""Functions in this file."""
# import string
import re


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome.

    Keyword arguments:
    text -- string to check for a palindrome
    """
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text: str) -> bool:
    """Check if a string is a palindrome using an iterative method.

    Keyword arguments:
    text -- string to check for a palindrome
    """
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


def is_palindrome_recursive(text: str,
                            left: int=None,
                            right: int=None) -> bool:
    """Check if a string is a palindrome using a recusive method.

    Keyword arguments:
    text -- string to check for a palindrome
    """
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


def string_contains_substring_iterative(string: str, substring: str) -> bool:
    """Check if a string contains a substring using an iterative method.

    Keyword arguments:
    string - base string that may or maynot contain a substring
    substring - string that may or maynot be contained in string
    """
    if len(string) < len(substring):
        return False

    for index in range(len(string)):
        if index + len(substring) < len(string)\
                and string[index:(index + len(substring))] == substring:
            return True
    return False


if __name__ == '__main__':
    print(string_contains_substring_iterative('cathether', 'cat'))
    string_contains_substring_iterative("string", "substring")
    is_palindrome_iterative("hello")
