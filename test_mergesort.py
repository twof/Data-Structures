#!python

from mergesort import merge_sort, async_merge_sort
import random
import unittest
import time


class MergesortTest(unittest.TestCase):

    def test_mergesort(self):
        ordered_arr = [1, 2, 3, 4, 5, 6, 7]
        unordered_arr = [77, 53, 68, 35, 69, 79, 72, 25, 82, 64]
        one_item_arr = [1]
        repeating_arr = [3, 3, 3, 3, 3]
        empty_arr = []
        assert merge_sort(ordered_arr) == ordered_arr
        assert merge_sort(unordered_arr)\
            == [25, 35, 53, 64, 68, 69, 72, 77, 79, 82]
        assert merge_sort(empty_arr) == []
        assert merge_sort(one_item_arr) == [1]
        assert merge_sort(repeating_arr) == [3, 3, 3, 3, 3]

    def test_async_mergesort(self):
        ordered_arr = [1, 2, 3, 4, 5, 6, 7]
        unordered_arr = [77, 53, 68, 35, 69, 79, 72, 25, 82, 64]
        one_item_arr = [1]
        repeating_arr = [3, 3, 3, 3, 3]
        empty_arr = []
        assert async_merge_sort(ordered_arr) == ordered_arr
        assert async_merge_sort(unordered_arr)\
            == [25, 35, 53, 64, 68, 69, 72, 77, 79, 82]
        assert async_merge_sort(empty_arr) == []
        assert async_merge_sort(one_item_arr) == [1]
        assert async_merge_sort(repeating_arr) == [3, 3, 3, 3, 3]

    def test_performance_mergesort(self):
        arr = random.sample(range(100000), 100)
        start = time.time()
        merge_sort(arr)
        end = time.time()
        print(end - start)

    def x_test_performance_async_mergesort(self):
        arr = random.sample(range(1000000), 1000)
        start = time.time()
        async_mergesort(arr)
        end = time.time()
        print(end - start)


if __name__ == '__main__':
    unittest.main()
