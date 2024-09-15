# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse
vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?


Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

class SparseVector:
    def __init__(self, nums: List[int]):


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
'''


class SparseVector:
    def __init__(self, nums):
        self.length = len(nums)
        self.sparse_dict = {}
        for i, el in enumerate(nums):
            if el:
                self.sparse_dict[i] = el

    def dotProduct(self, vec) -> int:
        if self.length != vec.length:
            raise Exception('Vectors should have equal length.')
        dot_product = 0
        for k in self.sparse_dict.keys():
            if k in vec.sparse_dict.keys():
                dot_product += self.sparse_dict.get(k) * vec.sparse_dict.get(k)
        return dot_product


if __name__ == '__main__':
    nums1 = [1, 0, 2]
    nums2 = [0, 2, 3]
    sv1 = SparseVector(nums1)
    sv2 = SparseVector(nums2)
    print(sv1.sparse_dict)
    print(sv2.sparse_dict)
    print(sv1.dotProduct(sv2))
