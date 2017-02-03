from linked_list import Linked_List
from cappedQueue import Queue
import string
import random


class HashTable(object):
    # O(n)
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        # lucas numbers (1, 3, 4, 7, 11...)
        # Check if a number is prime (5)
        # 5th lucas number (11) -1 is 10
        # check if 10 is a multiple of 5
        # True
        # Check if we're right with Lucas-Lehmer sequece
        # Goes like (4, 14, 194) square the previous and subtract 2
        # All Mersenne primes take the form 2^n - 1
        # Take n-1 and go to that position in the L-L list
        # See if that item is a multiple of the number we're checking
        # 2^3-1 = 7
        # 3-1 = 2
        # L-L[n-2] = 14
        # 14 is a multiple of 7
        # Lucas method in reverse:
        # len(_lucas_numbers)-1 % _lucas_numbers[len(_lucas_numbers)-1]-1 == 0
        self.current_buckets = init_size
        self._lucas_numbers = Queue(3)
        self._lucas_numbers.enqueue(1)
        self._lucas_numbers.enqueue(3)

        self._lucas_len = 2
        self.buckets = [None for i in range(self.current_buckets)]
        self.current_index = 0

    # O(1)
    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    # O(1)
    def __iter__(self):
        return self

    # O(1)
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    # O(n)
    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        total = 0

        for bucket in self.buckets:
            if bucket:
                total += bucket.length()

        return total

    # O(n)
    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        bucket = self.buckets[self._bucket_index(key)]

        if bucket.find(lambda item: item[0] == key) is not None:
            return True
        else:
            return False

    # O(n)
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        bucket = self.buckets[self._bucket_index(key)]
        found_item = bucket.find(lambda item: item[0] == key)

        if found_item is not None:
            return found_item[1]
        else:
            raise KeyError

    # O(n)
    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        bucket = self.buckets[self._bucket_index(key)]

        if bucket:
            item_list = self.items()
            item_list.append([key, value])
            self.optimize_buckets(item_list)
        else:
            self.buckets[self._bucket_index(key)] = Linked_List([[key, value]])

    # O(n)
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        bucket = self.buckets[self._bucket_index(key)]

        try:
            bucket.delete(key, lambda item: item[0] == key)
        except ValueError as e:
            raise KeyError

    # O(n + b)
    def keys(self):
        """Return a list of all keys in this hash table"""
        key_list = []

        for bucket in self.buckets:
            bucket_list = bucket.as_list(lambda data: data[0])
            key_list.extend(bucket_list)

        return key_list

    # O(n + b)
    def values(self):
        """Return a list of all values in this hash table"""
        val_list = []

        for bucket in self.buckets:
            bucket_list = bucket.as_list(lambda data: data[1])
            val_list.extend(bucket_list)

        return val_list

    def items(self):
        item_list = []

        for bucket in self.buckets:
            if bucket:
                bucket_list = bucket.as_list()
                item_list.extend(bucket_list)

        return item_list

    # defaults to buckets = number of items in the table
    def resize_table(self, item_list, size=None):
        if size is None:
            size = self.length()

        self.buckets = [None for i in range(size)]

        for item in item_list:
            self.set(item[0], item[1])

    def optimize_buckets(self, item_list):
        size = self._next_prime()

        self.resize_table(item_list, size)

    def print_table(self):
        for index, bucket in enumerate(self.buckets):
            print("bucket"+str(index))

            if bucket:
                bucket.print_list()

    def _next_prime(self):
        queue_len = len(self._lucas_numbers)

        self._lucas_numbers.enqueue(
            self._lucas_numbers[queue_len-1]
            + self._lucas_numbers[queue_len-2])

        queue_len = len(self._lucas_numbers)
        self._lucas_len += 1

        while not ((self._lucas_numbers[queue_len-1]-1)
                   % self._lucas_len == 0):
            self._lucas_numbers.enqueue(
                self._lucas_numbers[queue_len-1]
                + self._lucas_numbers[queue_len-2])

            queue_len = len(self._lucas_numbers)
            self._lucas_len += 1

        return self._lucas_len


if __name__ == '__main__':
    ht = HashTable(2)

    for i in range(1000):
        ht.set(''.join(random.choice(string.ascii_uppercase
                                     + string.digits)
                       for _ in range(20)), True)
    ht.print_table()
