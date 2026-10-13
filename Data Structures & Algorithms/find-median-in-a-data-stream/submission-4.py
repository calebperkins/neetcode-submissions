class MedianFinder:

    def __init__(self):
        # [.....max heap....] [.....min heap...]
        # A max heap
        self._left = []
        # A min heap
        self._right = []

    def addNum(self, num: int) -> None:
        # Invariant: top of self._max_heap < top of self._min_heap

        heapq.heappush_max(self._left, num)

        # Fix ordering between left and right
        if self._right and self._left[0] > self._right[0]:
            lft_v = self._pop_left()
            rgt_v = self._pop_right()

            self._push_left(rgt_v)
            self._push_right(lft_v)
        
        assert (not self._right) or (self._left[0] <= self._right[0])
        
        # Fix the sizes
        if len(self._left) - len(self._right) > 1:
            q = self._pop_left()
            self._push_right(q)
        elif len(self._right) - len(self._left) > 1:
            q = self._pop_right()
            self._push_left(q)
        
        assert abs(len(self._left) - len(self._right)) <= 1
    

    def _push_left(self, n):
        heapq.heappush_max(self._left, n)
    
    def _push_right(self, n):
        heapq.heappush(self._right, n)
    
    def _pop_left(self):
        return heapq.heappop_max(self._left)
    
    def _pop_right(self):
        return heapq.heappop(self._right)
    
    def findMedian(self) -> float:
        assert self._left or self._right, "not allowed to be called yet"
        if (len(self._left) + len(self._right)) % 2 == 0:
            return (self._left[0] + self._right[0]) / 2
        return self._left[0]
        
        