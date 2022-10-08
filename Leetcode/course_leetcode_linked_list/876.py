# https://leetcode.com/problems/middle-of-the-linked-list/
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]


if __name__ == '__main__':
    s = Solution()
    tests = [
        [
            [1, 2, 3, 4, 5],
            [3, 4, 5],
        ],
        [
            [1, 2, 3, 4, 5, 6],
            [4, 5, 6],
        ],
    ]
    for test in tests:
        # assert s.middleNode(test[0]) == test[1]
        s.middleNode(test[0])
