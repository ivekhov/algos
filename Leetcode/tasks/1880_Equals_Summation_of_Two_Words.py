# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/


class Solution:
    d = {
        'a': '0',
        'b': '1',
        'c': '2',
        'd': '3',
        'e': '4',
        'f': '5',
        'g': '6',
        'h': '7',
        'i': '8',
        'j': '9',
    }

    def calc_num(self, word):
        val_str = ''
        for i in word:
            val_str += self.d[i]
        return int(val_str)

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return (self.calc_num(firstWord) + self.calc_num(secondWord)) == self.calc_num(targetWord)


if __name__ == '__main__':
    firstWord = "acb"
    secondWord = "cba"
    targetWord = "cdb"


    # firstWord = "aaa"
    # secondWord = "a"
    # targetWord = "aaaa"
    s = Solution()
    print(s.isSumEqual(firstWord, secondWord, targetWord))

