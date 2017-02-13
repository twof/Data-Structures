#!python
from linkedlist import LinkedList


class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        self.list = LinkedList()

        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        return self.list.length == 0

    def length(self):
        """Return the number of items in this queue"""
        return self.list.length

    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        return self.list.head.data

    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        self.list.append(item)

    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError('stack is empty')
        else:
            val = self.list.head.data
            self.list.delete(val)
            return val
