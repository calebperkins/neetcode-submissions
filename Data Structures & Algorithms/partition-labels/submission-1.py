from collections import Counter


def partitions(string: str):
    remaining = Counter(string)
    used = set()
    window = 0
    output = []

    for i, char in enumerate(string):
        window += 1
        used.add(char)
        remaining[char] -= 1
        if all(remaining[c] == 0 for c in used):
            output.append(window)
            window = 0
            used.clear()

    return output


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return partitions(s)
