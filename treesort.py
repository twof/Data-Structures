import builtins
import random
from binarytree import BinarySearchTree

def tree_sort(self):
    return BinarySearchTree(self).inorder_list()


setattr(builtins.list, "tree_sort", tree_sort)

print(random.sample(range(100), 10).tree_sort())
