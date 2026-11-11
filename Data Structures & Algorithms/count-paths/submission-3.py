from functools import cache


def unique_paths(m, n):
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


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return unique_paths(m, n)
