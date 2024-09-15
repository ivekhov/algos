# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/ episode 49

from typing import List

class Solution:

    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for main_idx in range(len(boxes)):
            steps = 0
            for internal_idx in range(len(boxes)):
                if internal_idx == main_idx:
                    continue
                elif boxes[internal_idx] == '0':
                    continue
                else:
                    steps += abs(main_idx - internal_idx)
            res.append(steps)
        return res


if __name__ == '__main__':
    pass
    tests = [
        [
            "110",
            [1, 1, 3],
        ],
        [
            "001011",
            [11, 8, 5, 4, 3, 4],
        ],
    ]
    s = Solution()
    for test in tests:
        assert s.minOperations(test[0]) == test[1]
