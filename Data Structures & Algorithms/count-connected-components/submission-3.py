from dataclasses import dataclass


@dataclass
class Component:
    node: int
    parent: Component | None = None

    def root(self):
        r = self
        while r.parent and r.parent != r:
            r = r.parent
        return r

    def union(self, other):
        a, b = self.root(), other.root()
        if a is b:
            return
        smaller, bigger = (a, b) if a.node < b.node else (b, a)
        smaller.parent = bigger


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        components = {m: Component(m) for m in range(n)}
        for a, b in edges:
            c1 = components[a]
            c2 = components[b]
            c1.union(c2)

        return len({c.root().node for c in components.values()})
