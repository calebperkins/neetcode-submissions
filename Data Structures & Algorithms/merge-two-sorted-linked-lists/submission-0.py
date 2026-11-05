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
        head = ListNode(x.val)
        x = x.next
    else:
        head = ListNode(y.val)
        y = y.next
    tail = head

    while x and y:
        if x.val <= y.val:
            tail.next = ListNode(x.val)
            tail = tail.next
            x = x.next
        else:
            tail.next = ListNode(y.val)
            tail = tail.next
            y = y.next

    # append remaining, it doesn't matter what order because we exhausted one of them
    while x:
        tail.next = ListNode(x.val)
        tail = tail.next
        x = x.next

    while y:
        tail.next = ListNode(y.val)
        tail = tail.next
        y = y.next

    return head


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        return merge(list1, list2)
