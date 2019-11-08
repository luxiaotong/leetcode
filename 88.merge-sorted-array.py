#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i < m + n and j < n:
            if i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums2[j] >= nums1[i]:
                i += 1
            else:
                tmp = nums1[i]
                nums1[i] = nums2[j]
                nums2[j] = tmp
                nums2.sort()
                
                i += 1
                


# @lc code=end

s = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
nums2 = []
m = 1
n = 0
s.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
m = 3
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]
m = 6
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)