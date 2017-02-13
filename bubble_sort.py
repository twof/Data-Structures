import random


def bubble_sort(arr):
    while True:
        is_sorted = True
        for index in range(len(arr)-1):
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
                is_sorted = False
        if is_sorted:
            return arr


a = random.sample(range(10), 10)
print(bubble_sort(a))
