# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return is_same(p, q)


def is_same(p, q):
    if not p and not q:
        return True
    if p and not q:
        return False
    if not p and q:
        return False

    if p.val != q.val:
        return False
    return is_same(p.left, q.left) and is_same(p.right, q.right)
