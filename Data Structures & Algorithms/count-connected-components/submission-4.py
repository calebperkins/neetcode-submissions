from dataclasses import dataclass


@dataclass
class Component:
    node: int
    parent: Component | None = None
    size: int = 1

    def root(self):
        # First pass: find the root
        r = self
        while r.parent is not None:
            r = r.parent

        # Path compression: point every node on the path directly at the root
        x = self
        while x.parent is not None:
            next_node = x.parent
            x.parent = r
            x = next_node

        return r

    def union(self, other):
        a, b = self.root(), other.root()
        if a is b:
            return

        # Attach the smaller tree under the larger one
        smaller, bigger = (a, b) if a.size < b.size else (b, a)
        smaller.parent = bigger
        bigger.size += smaller.size


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        components = {m: Component(m) for m in range(n)}
        for a, b in edges:
            c1 = components[a]
            c2 = components[b]
            c1.union(c2)

        return len({c.root().node for c in components.values()})
