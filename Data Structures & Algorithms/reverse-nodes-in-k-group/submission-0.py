# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverse(head: ListNode, k: int) -> ListNode:
    # If there are fewer than k nodes left, leave the nodes as they are.
    h = head
    count = 0
    while h and count < k:
        count += 1
        h = h.next

    if count < k:
        return head

    new_head, new_tail = _reverse(head, k)

    new_tail.next = reverse(new_tail.next, k) if new_tail.next else None

    return new_head


def _reverse(head: ListNode, k: int) -> tuple[ListNode, ListNode]:
    if k <= 1:
        return head, head

    new_head, new_tail = _reverse(head.next, k - 1)

    rest = new_tail.next  # first node after the reversed block
    new_tail.next = head  # attach current node after the reversed part
    head.next = rest  # current node becomes the tail and links to the rest
    return new_head, head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return reverse(head, k)
