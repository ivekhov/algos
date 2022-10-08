from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None for item in range(len(s))]

        for idx in range(len(s)):
            res[indices[idx]] = s[idx]

        return ''.join(res)