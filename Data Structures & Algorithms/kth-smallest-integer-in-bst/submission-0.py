# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


# I don't think the fact we have a BST helps us. We don't how many elements are on one side of the tree,
# so we have to check each node.
def smallest(root: TreeNode, k: int):
    assert k >= 1

    def node_iterator():
        stack = [root]
        while stack:
            n = stack.pop()
            yield n
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

    k_smallest = heapq.nsmallest(k, node_iterator(), key=lambda n: n.val)
    return k_smallest[-1].val


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return smallest(root, k)
