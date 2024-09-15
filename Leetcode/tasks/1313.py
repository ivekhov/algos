class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        res = []
        arr_len = len(nums)
        for i in range(arr_len)[::2]:
            freq = nums[i]
            value = nums[i + 1]
            new = [value] * freq
            res += new
        return res