# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


if __name__ == '__main__':
    s = Solution()

    tests = [
        ['32', 3],
        ['82734', 8],
        ['27346209830709182346', 9]
    ]
    for test in tests:
        assert s.minPartitions(test[0]) == test[1]
        print(s.minPartitions(test[0]))

