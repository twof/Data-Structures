import random


def radix_sort(arr):
    buckets = [[] for n in range(10)]
    is_sorted = False
    place = 1

    while not is_sorted:
        for item in arr:
            sig_dig = item//10**(place-1) % 10
            buckets[sig_dig].append(item)

        arr = [item for sublist in buckets for item in sublist]

        is_sorted = True
        for bucket in buckets[1:]:
            if bucket:
                is_sorted = False
                break

        buckets = [[] for n in range(10)]
        place += 1
    return arr


a = random.sample(range(10), 10)
radix_sort(a)
