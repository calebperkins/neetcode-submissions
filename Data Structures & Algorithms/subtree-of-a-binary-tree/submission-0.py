# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def is_subtree(root: TreeNode, subroot: TreeNode) -> int:
    return any(is_equal(node, subroot) for node in node_iter(root))


def node_iter(root):
    stack = [root]
    while stack:
        n = stack.pop()
        yield n
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)


def is_equal(a, b):
    if a is None or b is None:
        return a is b
    return a.val == b.val and is_equal(a.left, b.left) and is_equal(a.right, b.right)


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return is_subtree(root, subRoot)
