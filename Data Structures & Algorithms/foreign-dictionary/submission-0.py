def alien_dict(words: list[str]) -> str:
    # letter => letters it precedes. e.g. A => {X, Y} implies A precides X and Y
    graph: dict[str, set[str]] = {}

    for word in words:
        for letter in word:
            if letter not in graph:
                graph[letter] = set()
    
    for a, b in zip(words, words[1:]):
        i = 0
        shorter_word_len = min(len(a), len(b))
        while i < shorter_word_len and a[i] == b[i]: 
            i += 1
        if i == shorter_word_len and len(a) > len(b):
            return "" # this list isn't valid
        if i < shorter_word_len:
            assert a[i] != b[i]
            graph[a[i]].add(b[i])
    
    # topologically sort the graph
    return topological_sort(graph)


def topological_sort(graph: dict[str, set[str]]) -> str:
    indegrees: dict[str, int] = {n: 0 for n in graph}
    for succ in graph.values():
        for b in succ:
            indegrees[b] += 1
    
    nodes_without_incoming = [n for n, incoming in indegrees.items() if incoming == 0] 
    output = []

    while nodes_without_incoming:
        n = nodes_without_incoming.pop()
        output.append(n)
        for successor in graph[n]:
            indegrees[successor] -= 1
            if indegrees[successor] == 0:
                nodes_without_incoming.append(successor)
    
    if len(output) < len(graph):
        return "" # a cycle exists or not every node is reachable
    return "".join(output)


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        return alien_dict(words)