#https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        counter = 0
        for i in stones:
            if i in jewels:
                counter += 1

        return counter


if __name__ == '__main__':
    s = Solution()

    tests = [
        ["aA", "aAAbbbb", 3],
        ["z", "ZZ", 0],
    ]
    for test in tests:
        assert test[2] == s.numJewelsInStones(test[0], test[1])
