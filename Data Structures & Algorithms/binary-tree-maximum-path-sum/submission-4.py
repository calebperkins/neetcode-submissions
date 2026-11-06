# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache


@cache
def _max_sum(node: TreeNode | None) -> int:
    # the max sum with this node as the root
    if not node:
        return 0
    # take root plus left child, right child, or neither
    return node.val + max(0, _max_sum(node.left), _max_sum(node.right))


def max_path_sum(root: TreeNode) -> int:
    stack = [root]
    best = root.val
    while stack:
        n = stack.pop()
        l = _max_sum(n.left) if n.left else 0
        r = _max_sum(n.right) if n.right else 0

        # best path passing through this node...
        # take both, take just left, take just right, take neither
        result = max(l + r + n.val, l + n.val, n.val + r, n.val)
        best = max(best, result)

        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)
    return best


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max_path_sum(root) if root else 0
