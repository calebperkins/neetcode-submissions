class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return group_anagrams(strs)


def group_anagrams(strs: list[str]):
    grouped: dict[str, list[str]] = {}
    for s in strs:
        key = "".join(sorted(s))
        group = grouped.setdefault(key, [])
        group.append(s)
    return list(grouped.values())
