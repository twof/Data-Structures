import random


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = arr.index(min(arr[i:]))
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


a = random.sample(range(10), 10)
print(selection_sort(a))
