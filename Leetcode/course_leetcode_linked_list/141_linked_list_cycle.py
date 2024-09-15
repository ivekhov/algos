# https://leetcode.com/problems/linked-list-cycle/

# my version - wrong
# find last
# check its link on element with pos index

# correct is below


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional, List

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False

    def has_cycle_pointers(self, head):
        if head is None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def solution(self, head):
        if head is None: return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next


        return True

if __name__ == '__main__':
    print(42)