from collections import Counter


def partitions(string: str):
    counter = Counter(string)
    used = Counter()
    window = 0
    output = []

    for i, char in enumerate(string):
        window += 1
        used[char] += 1
        counter[char] -= 1
        if all(counter[c] == 0 for c in used):
            output.append(window)
            window = 0

    return output


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return partitions(s)
