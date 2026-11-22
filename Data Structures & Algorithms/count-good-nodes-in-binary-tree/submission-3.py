# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def good_nodes(root: TreeNode) -> int:
    good = 0
    stack = [(root, root.val)]

    while stack:
        n, max_so_far = stack.pop()
        if n.val >= max_so_far:
            good += 1
        new_max = max(max_so_far, n.val)
        if n.left:
            stack.append((n.left, new_max))
        if n.right:
            stack.append((n.right, new_max))

    return good


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return good_nodes(root)
