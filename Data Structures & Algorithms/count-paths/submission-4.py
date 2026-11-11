from functools import cache


def unique_paths_recursive(m, n):
    @cache
    def _count_paths(cell):
        i, j = cell
        if not (0 <= i < m):
            return 0
        if not (0 <= j < n):
            return 0
        if cell == (m - 1, n - 1):
            return 1
        return _count_paths((i + 1, j)) + _count_paths((i, j + 1))

    return _count_paths((0, 0))


def unique_paths(m, n):
    # how many paths starting from point (i, j)
    paths = {(i, j): None for i in range(m) for j in range(n)}
    for row in range(m):
        paths[row, n - 1] = 1
    for col in range(n):
        paths[m - 1, col] = 1

    for row in reversed(range(m - 1)):
        for col in reversed(range(n - 1)):
            paths[row, col] = paths[row + 1, col] + paths[row, col + 1]
    return paths[0, 0]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return unique_paths(m, n)
