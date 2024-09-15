from re import L
from typing import List


class Solution:
    def createTargetArray(self, nums, index):
        res = []

        for idx in range(len(nums)):
            res.insert(index[idx], nums[idx])
            

        return res


if __name__ == '__main__':
    s = Solution()

    tests = [
        [
            [0,1,2,3,4],
            [0,1,2,2,1],
            [0,4,1,3,2],
        ], 
        [
            [1,2,3,4,0],
            [0,1,2,3,0], 
            [0,1,2,3,4],
        ],
        [
            [1],
            [0],
            [1],
        ]
    ]

    # for test in tests:
    #     print(s.createTargetArray(test[0], test[1]))

    for test in tests:
        assert s.createTargetArray(test[0], test[1]) == test[2]
