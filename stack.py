#!python
from linkedlist import LinkedList

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        self.list = LinkedList()

        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        return self.list.length == 0

    def length(self):
        """Return the number of items in this stack"""
        return self.list.length

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        return self.list.head

    def push(self, item):
        """Push the given item onto this stack"""
        self.list.prepend(item)

    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError('stack is empty')
        else:
            val = self.list.head.data
            self.list.delete(val)
            return val
