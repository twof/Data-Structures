"""
**Challenges:**
- implement binary search tree with node objects
- implement search, insert, delete binary search tree operations
- implement iterative and recursive binary search tree traversals
- implement map (dictionary) with binary search tree
- annotate functions with complexity analysis
- stretch: implement binary search tree with singly linked list
- stretch: implement n-ary search tree with dynamic array
"""
from enum import Enum


class _Node:
    def __init__(self, value, left=None, right=None, middle=None):
        self.value = [value]
        self.left = left
        self.right = right
        self.middle = middle

    def __repr__(self):
        return "Node(" + str(self.value)\
            + ", " + str(self.left)\
            + ", " + str(self.right) + ")"


class _Side(Enum):
    RIGHT = 1
    LEFT = 2
    MID = 3


class TwoTreeTree:

    def __init__(self):
        self.head = None

    def search(self, value):
        current_node = self.head

        while True:
            if current_node is None:
                return False
            elif current_node.value == value:
                return True
            elif current_node.value < value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def insert(self, value, node=None):
        if self.head is None:
            self.head = _Node(value)
            return

        if node is None:
            node = self.head

        if len(node.value) == 1:
            if value < node.value:
                if node.left is None:
                    node.left = _Node(value)
                    return
                else:
                    node.left.value.append(value)
                    node.left.value = sorted(node.left.value)

                    if len(node.left.value) == 3:
                        mid = node.left.value.pop(1)
                        node.value.append(mid)
                        node.value = sorted(node.value)
            elif value >= node.value:
                if node.right is None:
                    node.right = _Node(value)
                    return
                else:
                    node.left.value.append(value)
                    node.left.value = sorted(node.left.value)

    def delete(self, value):
        current_node = self.head
        next_node = not None
        side = _Side.LEFT

        if current_node is None:
            raise ValueError
        else:
            while(next_node is not None):
                if current_node.value < value:
                    next_node = current_node.left
                    side = _Side.LEFT

                    if next_node is None:
                        break
                elif current_node.value > value:
                    next_node = current_node.right
                    side = _Side.RIGHT

                    if next_node is None:
                        break
                else:

                    current_node = next_node

            if side == _Side.LEFT:
                current_node.left = _Node(value)
            else:
                current_node.right = _Node(value)

    def preorder_traversal(self, node):
        """Recursive pre order traversal starting from an arbitrary _Node.

        Complexity: O(n)
        """
        if node is None:
            return

        print(node.value, end=', ')
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        """Recursive in order traversal starting from an arbitrary _Node.

        Complexity: O(n)
        """
        if node is None:
            return

        self.inorder_traversal(node.left)
        print(node.value, end=', ')
        self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        """Recursive post order traversal starting from an arbitrary _Node.

        Complexity: O(n)
        """
        if node is None:
            return

        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.value, end=', ')




def main():
    bst = TwoTreeTree()
    print(bst.head)
    bst.insert(10)
    print(bst.head)
    bst.insert(5)
    bst.insert(12)
    bst.insert(20)
    bst.insert(1)
    bst.insert(3)
    bst.insert(13)
    print(bst.head)
    print(bst.head.left)
    print(bst.head.right)

    print("---searching---")
    print(bst.search(5))
    print(bst.search(12))
    print(bst.search(8))

    print("Preorder: ")
    bst.preorder_traversal(bst.head)
    print('\n', end='')
    print("In Order: ")
    bst.inorder_traversal(bst.head)
    print('\n', end='')
    print("Postorder: ")
    bst.postorder_traversal(bst.head)


if __name__ == '__main__':
    main()
