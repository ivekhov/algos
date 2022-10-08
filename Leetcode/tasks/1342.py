# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        temp = num
        while temp != 0:
            if temp % 2 == 0:
                temp = temp / 2
            elif temp % 2 == 1:
                temp = temp - 1
            counter += 1
        return counter


if __name__ == '__main__':
    s = Solution()
    tests = [
        [14, 6],
        [8, 4],
        [123, 12],
    ]
    for test in tests:
        assert s.numberOfSteps(test[0]) == test[1]