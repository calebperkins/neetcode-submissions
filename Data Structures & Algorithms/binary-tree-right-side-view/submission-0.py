# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


def right_side_view(root):
    r = []
    queue = deque()

    if root:
        queue.append(root)

    while queue:
        x = len(queue)
        last = queue[-1]
        for _ in range(x):
            n = queue.popleft()
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        r.append(n.val)

    return r


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return right_side_view(root)
