# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def level_order(root: TreeNode | None) -> list[list[int]]:
    results = []

    queue = deque()
    if root:
        queue.append(root)

    while queue:
        current_level = []
        in_this_level = len(queue)
        for _ in range(in_this_level):
            n = queue.popleft()
            current_level.append(n.val)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        results.append(current_level)
    return results


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        return level_order(root)
