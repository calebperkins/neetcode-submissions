import bisect

def _find_pivot(xs: list[int]) -> int:
    # return the index of the first value that is out of order, e.g. less than xs[0]
    # [T, T, T, F, F]  xs[i] >= xs[0]
    
    lo = 0
    hi = len(xs) - 1
    
    while hi - lo > 1:
        m = lo + (hi - lo) // 2

        if xs[m] >= xs[0]:
            lo = m
        else:
            hi = m

    return hi # [T, F] we are getting the out of order element, the F

def search(xs: list[int], target: int) -> int:
    assert xs
    pivot = _find_pivot(xs)

    if pivot == 0: # array is fully rotated 
        i = bisect.bisect_left(xs, target)
    if xs[0] <= target: # go left of pivot
        i = bisect.bisect_left(xs, target, hi=pivot)
    else: # go right of pivot
        i = bisect.bisect_left(xs, target, lo=pivot)
    
    if i < len(xs) and xs[i] == target:
        return i
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search(nums, target)