# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import cache

def node_iter(node):
    yield node

    if node.left:
        yield node.left
    
    if node.right:
        yield node.right


def _diameter(node):
    # the diameter passing through _this_ node
    if node is None:
        return 0
    
    return _height(node.left) + _height(node.right)

def diameter(root: TreeNode) -> int:
    return max(_diameter(node) for node in node_iter(root))

@cache
def _height(node):
    if node is None:
        return 0
    return 1 + max(_height(node.left), _height(node.right))

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return diameter(root)