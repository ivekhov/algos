# https://leetcode.com/problems/subrectangle-queries/

'''
Your SubrectangleQueries object will be instantiated and called as such:
obj = SubrectangleQueries(rectangle)
obj.updateSubrectangle(row1,col1,row2,col2,newValue)
param_2 = obj.getValue(row,col)
'''

from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


if __name__ == '__main__':
    rec = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
    sq = SubrectangleQueries(rec)
    print(sq.rectangle)
    print(sq.getValue(0, 1))
    sq.updateSubrectangle(0, 0, 3, 2, 5)
    print(sq.rectangle)
