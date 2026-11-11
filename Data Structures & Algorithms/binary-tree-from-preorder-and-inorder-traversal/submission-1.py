# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    preorder = iter(TreeNode(v) for v in preorder)

    # Maps value to the index in the inorder array.
    inorder_index = {}
    for i, v in enumerate(inorder):
        inorder_index[v] = i

    def build(i, j):  # j exclusive
        if i == j:
            return None

        root = next(preorder)
        root_i = inorder_index[root.val]
        root.left = build(i, root_i)
        root.right = build(root_i + 1, j)

        return root

    return build(0, len(inorder))


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        return build_tree(preorder, inorder)
