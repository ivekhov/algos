# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string_value = ''
        for item in head:
            string_value += str(item)
        return int(string_value, 2)

'''
        string_value = ''
        current_value = head.val
        next_value = head.next

        while next_value:
            string_value += str(next_value.val)
            current_value = next_value.next

        return int(string_value, 2)
'''


if __name__ == '__main__':
    s = Solution()
    tests = [
        [[1, 0, 1], 5],
        [[0], 0]
    ]
    for test in tests:
        assert s.getDecimalValue(test[0]) == test[1]