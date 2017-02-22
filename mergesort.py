import random
from concurrent.futures import ProcessPoolExecutor, wait, as_completed


def split(arr_len, left, right, item):
    index = item[0]
    num = item[1]

    if index < arr_len/2:
        left.append(num)
    else:
        right.append(num)


def async_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = arr[:(len(arr)/2)]
    right = arr[(len(arr)/2):]

    left = async_merge_sort(left)
    right = async_merge_sort(right)
    return merge(left, right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []

    left = arr[:(len(arr)/2)]
    right = arr[(len(arr)/2):]

    left = merge_sort(left)
    right = merge_sort(right)

    with ProcessPoolExecutor() as executor:
        future = executor.submit(merge, left, right)
        return future.result()

def merge(left, right):
    result = []

    while left != [] and right != []:
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    if left != []:
        result.extend(left)
    elif right != []:
        result.extend(right)
    return result


# def async_merge(left, right):
#     result = []
#
#     with ProcessPoolExecutor() as executor:
#         # futures =


if __name__ == '__main__':
    a = [77, 53, 68, 35, 69, 79, 72, 25, 82, 64]
    print(merge_sort(a))
