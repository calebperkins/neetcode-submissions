# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return validate(root)


def validate(root):
    def _valid(n, s, e):
        if not n:
            return True
        if not (s < n.val < e):
            return False
        return _valid(n.left, s, n.val) and _valid(n.right, n.val, e)

    if not root:
        return True
    return _valid(root.left, float("-inf"), root.val) and _valid(root.right, root.val, float("inf"))
