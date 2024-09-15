# https://leetcode.com/problems/deepest-leaves-sum/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        pass

def build_tree(nodes):
    root = TreeNode(root[0])
    for val in nodes[1:]:
        # 



if __name__ == '__main__':
    s = Solution()
    nodes = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    root = None



    tests = [
        [
            [1,2,3,4,5,None,6,7,None,None,None,None,8],
            15,
        ],
        [
            [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5],
            19,
        ],
    ]
    # for test in tests:
    #     assert s.calculateTime(test[0]) == test[1]
