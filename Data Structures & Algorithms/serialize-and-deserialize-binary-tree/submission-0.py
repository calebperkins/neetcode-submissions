# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def serialize(root):
    tokens = []
    stack = deque([root])
    while stack:
        n = stack.pop()
        if n:
            tokens.append(str(n.val))
            stack.append(n.right)
            stack.append(n.left)
        else:
            tokens.append("N")
    return ",".join(tokens)


def deserialize(data):
    raw_tokens = data.split(",")
    tokens = [None if t == "N" else TreeNode(int(t)) for t in raw_tokens]
    tokens = iter(tokens)

    def build():
        t = next(tokens)
        if t is None:
            return
        t.left = build()
        t.right = build()
        return t

    return build()


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode | None) -> str:
        return serialize(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode | None:
        return deserialize(data)
