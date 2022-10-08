# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List
from math import sqrt


class Solution:
    def calc_distance(self, point_1, point_2):
        a = point_2[0] - point_1[0]
        b = point_2[1] - point_1[1]
        return sqrt(a ** 2 + b ** 2)

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            counter = 0
            for point in points:
                dist = self.calc_distance(point, query[:2])
                if dist <= query[2]:
                    counter += 1
            res.append(counter)
        return res


if __name__ == '__main__':
    tests = [
        [
            [[1, 3], [3, 3], [5, 3], [2, 2]],
            [[2, 3, 1], [4, 3, 1], [1, 1, 2]],
            [3, 2, 2]
        ],
        [
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
            [[1,2,2],[2,2,2],[4,3,2],[4,3,3]],
            [2, 3, 2, 4]
        ],
    ]
    s = Solution()
    for test in tests:
        assert s.countPoints(test[0], test[1]) == test[2]

    # r = s.countPoints(tests[0][0], tests[0][1])
    # print(r)
