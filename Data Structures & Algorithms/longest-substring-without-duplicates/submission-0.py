from collections import deque


def longest_substring(s):
    best = 0
    window = deque()
    contents = set()  # uniq chars in window

    for sub in s:
        while sub in contents:
            x = window.popleft()
            contents.remove(x)
        contents.add(sub)
        window.append(sub)
        best = max(best, len(window))

    return best


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return longest_substring(s)
