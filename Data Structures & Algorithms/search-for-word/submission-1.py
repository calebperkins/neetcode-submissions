

def word_search(board: list[list[str]], word: str) -> bool:
    visited: set[tuple[int, int]] = set()

    # A stack of (i, j, word index, whether to do cleanup)
    stack: list[tuple[int, int, int, bool]] = []

    def _neighbors(i, j):
        deltas = [(0, 1), (0, -1), (1,0), (-1, 0)]
        for di, dj in deltas:
            ni = i + di
            nj = j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                yield ni, nj

    for i, row in enumerate(board):
        for j in range(len(row)):
            stack.append((i, j, 0, False))
    
    while stack:
        i, j, w_i, deadend = stack.pop()

        if deadend:
            visited.remove((i, j))
            continue

        if (i, j) in visited or board[i][j] != word[w_i]:
            continue  

        if w_i == len(word) - 1:
            return True
        visited.add((i, j))
        stack.append((i, j, w_i, True))
        for x, y in _neighbors(i, j):
            stack.append((x, y, w_i + 1, False))

    return False


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        return word_search(board, word)