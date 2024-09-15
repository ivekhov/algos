# https://leetcode.com/problems/number-of-good-pairs/

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum_good = 0

        for idx in range(len(nums)):
            for j in range(len(nums)):
                if nums[idx] == nums[j] and idx < j:
                    sum_good += 1
        return sum_good


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    nums = [1,1,1,1]
    nums = [1, 2, 3]
    s = Solution()
    print(s.numIdenticalPairs(nums))
