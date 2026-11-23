def subsets(nums: list[int]):
    results = []
    num_bits = len(nums)

    # counter is a bit mask of what elements to pick
    for counter in range(2 ** num_bits):
        bits = ((counter >> bit) & 1 for bit in range(num_bits - 1, -1, -1))
        subset = [n for n, use_it in zip(nums, bits) if use_it]
        results.append(subset)
    
    return results


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return subsets(nums)