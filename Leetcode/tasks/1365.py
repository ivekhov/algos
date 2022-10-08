# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            counter = 0
            for j in nums:
                if i > j:
                    counter += 1
            res.append(counter)
        return res


if __name__ == '__main__':
    tests = [
        [
            [6, 5, 4, 8],
            [2, 1, 0, 3]
        ],
        [
            [7, 7, 7, 7],
            [0, 0, 0, 0]
        ],
    ]
    s = Solution()
    for test in tests:
        assert s.smallerNumbersThanCurrent(test[0]) == test[1]
