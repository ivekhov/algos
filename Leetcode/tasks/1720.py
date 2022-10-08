class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        res = [first]
        decoded_index = 0
        for item in encoded:
            res.append(item ^ res[decoded_index])
            decoded_index += 1
        return res