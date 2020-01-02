#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#
import random
import copy
# @lc code=start
class Solution:

    def __init__(self, nums: []):
        self.data = nums
        self.orig = list(nums)
        

    def reset(self) -> []:
        """
        Resets the array to its original configuration and return it.
        """
        self.data = self.orig
        self.orig = list(self.orig)
        return self.data
        

    def shuffle(self) -> []:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.data)):
            j = random.randint(i, len(self.data)-1)
            self.data[i], self.data[j] = self.data[j], self.data[i]
        return self.data

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end


