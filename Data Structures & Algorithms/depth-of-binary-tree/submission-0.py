# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive version
def max_depth_recursive(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Stack version
def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    best = 0
    stack: list[tuple[TreeNode, int]] = []
    if root is not None:
        stack.append((root, 1))
    while stack:
        n, current_depth = stack.pop()
        best = max(best, current_depth)
        if n.left:
            stack.append((n.left, current_depth + 1))
        if n.right:
            stack.append((n.right, current_depth + 1))

    return best


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return max_depth(root)
