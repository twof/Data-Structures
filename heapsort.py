from heap import MinHeap


def heap_sort(arr):
    heap = MinHeap(arr)
    return [heap.remove_min() for _ in arr]


if __name__ == '__main__':
    print(heap_sort([9, 25, 86, 3, 29, 5, 55]))
    print(heap_sort([]))
