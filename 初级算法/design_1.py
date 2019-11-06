#!/usr/bin/python
#coding:utf-8
import random

# Shuffle an Array
# 打乱一个没有重复元素的数组。

# 示例:
# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();

# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();

# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();



class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.output = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.output)
        for i in range(n):
            j = random.randint(i,n-1)#每次随机一个下标，和当前下标的交换
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output



# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5,6]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)
