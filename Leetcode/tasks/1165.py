# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        counter = 0
        start = 0
        for idx in range(len(word)):
            symbol = word[idx]
            for internal_idx in range(len(keyboard)):
                if keyboard[internal_idx] == symbol:
                    counter += abs(internal_idx - start)
                    start = internal_idx
        return counter

    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i, c in enumerate(keyboard):
            d[c] = i

        time = 0
        cur = 0
        for c in word:
            new = d[c]
            time = time + abs(cur - new)
            cur = new
        return time


if __name__ == '__main__':
    pass
    s = Solution()
    tests = [
        ["abcdefghijklmnopqrstuvwxyz", "cba", 4],
        ["pqrstuvwxyzabcdefghijklmno", "leetcode", 73],
    ]
    for test in tests:
        assert s.calculateTime(test[0], test[1]) == test[2]
