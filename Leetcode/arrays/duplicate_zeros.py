from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # ToDo  - wrong way
        # def shift_arr(array):
        #     end = len(array)
        #     for index in list(range(0, end))[::-1]:
        #         array[index] = array[index-1]
        #     array[0] = 0

        # looping through list
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                
                # wrong way
                # temp = arr[i+1:].copy()
                # shift_arr(temp)
                # arr = arr[:i+1] + temp
                # shift_arr(arr[i+1:])

                arr.pop()
                arr.insert(i, 0)

                i = i + 1
            i = i + 1

            
if __name__ == '__main__':
    tests = [
        [
            [1,0,2,3,0,4,5,0],
            [1,0,0,2,3,0,0,4],
        ],
        [
            [1,2,3],
            [1,2,3]
        ]
    ]
    s = Solution()
    for test in tests:
        s.duplicateZeros(test[0])
        # print(test[0])
        # print(test[1])
        assert test[0] == test[1]

