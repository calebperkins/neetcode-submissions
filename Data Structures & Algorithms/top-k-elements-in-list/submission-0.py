import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return top_k_frequent(nums, k)


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    largest = heapq.nlargest(k, ((c, n) for n, c in counts.items()))
    return [n for _, n in largest]
