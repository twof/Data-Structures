#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array)-1:
        return None
    elif item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1
    middle = (left + right)/2

    while left <= right:
        if array[middle] == item:
            return middle
        elif array[middle] > item:
            right = middle - 1
            middle = (left + right)/2
        elif array[middle] < item:
            left = middle + 1
            middle = (left + right)/2

    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left is None or right is None:
        left = 0
        right = len(array) - 1

    middle = (left + right)/2

    if array[middle] == item:
        return middle
    elif left > right:
        return None
    elif array[middle] > item:
        return binary_search_recursive(array, item, left, middle - 1)
    elif array[middle] < item:
        return binary_search_recursive(array, item, middle + 1, right)
