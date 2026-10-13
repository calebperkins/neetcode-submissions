import heapq

def buy_chocolate(prices, money):
    k = 2 # the number of pieces to buy
    heap = [] # max heap of size k 
    for price in prices:
        if len(heap) < k:
            heapq.heappush_max(heap, price)
        elif price < heap[0]:
            heapq.heapreplace_max(heap, price)
    
    s = sum(heap)
    return money - s if s <= money else money


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return buy_chocolate(prices, money)