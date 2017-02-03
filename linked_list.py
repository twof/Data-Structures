class Node:
    # O(1)
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_List:
    # O(n) where n is len(arr)
    def __init__(self, arr=None):
        self.count = 0
        self.head = None
        self.tail = None
        self.current_node = self.head

        if arr is not None:
            for item in arr:
                self.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node is None:
            print("hit")
            raise StopIteration
        else:
            node_to_return = self.current_node
            self.current_node = self.current_node.next
            return node_to_return

    # O(1)
    def append(self, data):
        new_node = Node(data, None)

        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    # O(1)
    def prepend(self, data):
        new_node = Node(data, None)

        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1

    # O(n) assuming filter_func is O(1)
    def upsert_first(self, data,
                     filter_func=None):
        if filter_func is None:
            def filter_func(item): return item == data

        if self.find(filter_func) is None:
            self.append(data)
            return
        else:
            current_node = self.head

            while current_node is not None:
                if filter_func(current_node.data):
                    current_node.data = data
                    return
                elif current_node.next is not None:
                    current_node = current_node.next
                    continue

    # This is really dirty and needs to be cleaned up
    # O(n) assuming filter_func is O(1)
    def delete(self, data, filter_func=None):
        found = False
        found_node = None
        prev_found_node = None

        if filter_func is None:
            def filter_func(item): return item == data

        if self.count == 0:
            raise ValueError
        else:
            current_node = self.head

            while current_node is not None:
                if filter_func(current_node.data):
                    found = True
                    found_node = current_node
                    prev_found_node = None
                    break
                elif filter_func(current_node.next.data):
                    found = True
                    found_node = current_node.next
                    prev_found_node = current_node
                    break
                else:
                    current_node = current_node.next
                    continue

            if self.count == 1 and found:
                self.count -= 1
                self.head = None
                self.tail = None
                return

            if found and found_node == self.tail:
                self.tail = prev_found_node
                prev_found_node.next = None
                self.count -= 1
            elif found and found_node == self.head:
                self.head = found_node.next
                self.count -= 1
            elif found:
                self.count -= 1
                prev_found_node.next = found_node.next
            elif not found:
                raise ValueError
            else:
                print("unhandled edge case")

    # O(n) assuming filter_func is O(1)
    def find(self, filter_func):
        if self.count == 0:
            return None
        else:
            current_node = self.head

        if filter_func(current_node.data):
            return current_node.data

        while current_node.next is not None:
            if filter_func(current_node.data):
                return current_node.data
            elif filter_func(current_node.next.data):
                return current_node.next.data
            else:
                current_node = current_node.next
                continue

        return None

    # O(n) assuming filter_func is O(1)
    def as_list(self, array_builder=None):
        listed = []

        if array_builder is None:
            def array_builder(item): return item

        if self.count == 0:
            return listed
        else:
            current_node = self.head
            listed.append(array_builder(current_node.data))

            while current_node.next is not None:
                listed.append(array_builder(current_node.next.data))
                current_node = current_node.next

            return listed

    # O(n) assuming filter_func is O(1)
    def print_list(self, print_func=None):
        if print_func is None:
            def print_func(data): print(data)

        if self.count == 0:
            return
        else:
            print_func(self.head.data)
            current_node = self.head

            while current_node.next is not None:
                print_func(current_node.next.data)
                current_node = current_node.next

    def length(self):
        return self.count
