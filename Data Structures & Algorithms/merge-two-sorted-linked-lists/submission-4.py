import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def merge(x: ListNode | None, y: ListNode | None) -> ListNode | None:
    if not x:
        return y
    if not y:
        return x
    assert x and y

    if x.val <= y.val:
        head = x
        x = x.next
    else:
        head = y
        y = y.next
    tail = head
    tail.next = None

    # we need a thunk to dedupe identical values because comparing ListNode doesn't work
    heap: list[tuple[int, int, ListNode]] = []
    if x:
        heapq.heappush(heap, (x.val, id(x), x))
    if y:
        heapq.heappush(heap, (y.val, id(y), y))

    while heap:
        assert tail.next is None

        _, _, lst = heapq.heappop(heap)
        assert lst
        tail.next = lst
        tail = tail.next

        if lst.next:
            heapq.heappush(heap, (lst.next.val, id(lst.next), lst.next))

        tail.next = None
    return head


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        return merge(list1, list2)
