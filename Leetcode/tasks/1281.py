from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        int_arr = []
        int_arr = [int(item) for item in str(n)]
        temp_sum, multi = 0, 1
        for item in int_arr:
            temp_sum += item
            multi *= item
        return multi - temp_sum