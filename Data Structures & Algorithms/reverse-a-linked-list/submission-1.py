# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        return reverse_list(head)

# Recursive version using O(n) space
def reverse_list_naive(head: ListNode | None) -> ListNode | None:
    # returns the head and tail
    def _reverse(h) -> tuple[ListNode, ListNode]:
        if h.next is None:
            return h, h
        sub_head, sub_tail = _reverse(h.next)
        assert sub_tail.next is None
        sub_tail.next = h
        h.next = None
        return sub_head, h
    
    if head is None: return None
    
    return _reverse(head)[0]


# tail recursive version using O(1) space
def reverse_list(head: ListNode | None) -> ListNode | None:
    if head is None: return None

    prev = None
    to_process = head
    
    while to_process:
        succ = to_process.next
        to_process.next = prev
        prev = to_process
        to_process = succ 
    
    return prev


