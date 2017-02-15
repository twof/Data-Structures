from binarytree import BinarySearchTree
import random


def tree_sort(arr):
    return BinarySearchTree(arr).inorder_list()


a = random.sample(range(100), 10)
print(tree_sort(a))
