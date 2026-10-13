from dataclasses import dataclass

@dataclass
class Node:
    value: str | None
    children: dict[str, 'Node']
    parent: object | None


def build_trie(words: list[str]) -> Node:
    root = Node(value=None, children={}, parent=None)
    for word in words:
        n = root
        for char in word:
            if char not in n.children:
                n.children[char] = Node(value=None, children={}, parent=n)
            n = n.children[char]
        n.value = word
    return root

def find_words(board, words):
    present = set()
    trie = build_trie(words)
    rows = len(board)
    cols = len(board[0]) if board else 0
    stack = [(i, j, trie, False) for i in range(rows) for j in range(cols)]
    used = set()

    def adjacent(i, j):
        x = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for di, dj in x:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                yield ni, nj

    while stack:
        i, j, t, cleanup = stack.pop()
        if cleanup:
            used.remove((i, j))
            continue
        if (i, j) in used:
            continue
        letter = board[i][j]
        if letter not in t.children:
            continue
        
        t = t.children[letter]
        if t.value:
            present.add(t.value)
        used.add((i, j))
        stack.append((i, j, t, True))
        for di, dj in adjacent(i, j):
            stack.append((di, dj, t, False))
    
    return present


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        return list(find_words(board, words))