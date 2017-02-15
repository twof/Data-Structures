import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []

    for index, item in enumerate(arr):
        if index < len(arr)/2:
            left.append(item)
        else:
            right.append(item)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left != [] and right != []:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left != []:
        result.extend(left)
    elif right != []:
        result.extend(right)
    return result


a = random.sample(range(100), 10)
print(merge_sort(a))
