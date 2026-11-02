import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return merge_k_lists(lists)


def merge_k_lists(nodes):
    heap = [(ll.val, i, ll) for i, ll in enumerate(nodes) if ll]
    heapq.heapify(heap)

    # start of the merged output
    merged_head = None

    # where to append entries
    merged_tail = None
    
    while heap:
        v, i, ll = heapq.heappop(heap)

        if merged_tail:
            merged_tail.next = ListNode(v, None)
            merged_tail = merged_tail.next
        else:
            merged_head = ListNode(v, None)
            merged_tail = merged_head

        if ll.next:
            ll = ll.next
            heapq.heappush(heap, (ll.val, i, ll))
    
    return merged_head
