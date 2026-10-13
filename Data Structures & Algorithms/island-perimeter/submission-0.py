LAND = 1
WATER = 0

def grid_to_graph(grid):
    def neighbors(node):
        i, j = node
        perms = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in perms:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] == LAND:
                    yield ni, nj

    g = {}
    start = None
    for i, row in enumerate(grid):
        for j, land_or_water in enumerate(row):
            if land_or_water == LAND:
                g[i, j] = set()
    assert g is not None

    for node in g.keys():
        for neighbor in neighbors(node):
            g[node].add(neighbor)
            g[neighbor].add(node)

    return g


def island_perimeter(graph):
    c = 0
    for n in graph.values():
        c += 4 - len(n)
    return c


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return island_perimeter(grid_to_graph(grid))