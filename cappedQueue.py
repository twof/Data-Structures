# Standard FIFO Queue with a fixed size
class Queue:
    def __init__(self, size_cap):
        self.size_cap = size_cap  # maximum size of the queue
        self.contents = []  # a list is used to hold the contents of the Queue
        self.len = 0

    def __len__(self):
        return self.len

    def __getitem__(self, key):
        if self.len > key:
            return self.contents[key]
        else:
            raise IndexError('Queue index out of range')

    def __repr__(self):
        return str(self.contents)

    def enqueue(self, item):  # appends an `item` to the end of the queue
        self.contents.append(item)
        self.len += 1

        if len(self.contents) > self.size_cap:  # if the max size of the queue
                                                # is reached
            self.contents.pop(0)  # remove the first item in the array
            self.len -= 1
