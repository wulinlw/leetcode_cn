#!/usr/bin/python
#coding:utf-8

# 面试题 17.04. 消失的数字
# 数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？
# 注意：本题相对书上原题稍作改动
# 示例 1：
# 输入：[3,0,1]
# 输出：2
 

# 示例 2：
# 输入：[9,6,4,2,3,5,7,0,1]
# 输出：8
# https://leetcode-cn.com/problems/missing-number-lcci/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        re = 0
        for i in range(n+1):
            re = re+i
            if i<n:
                re -= nums[i]
        return re

    #2次异或等于本身
    def missingNumber2(self, nums: List[int]) -> int:
       res = 0
       for i in range(len(nums)):
           res ^= i
           res ^=nums[i]
       res ^= len(nums)         #前面长度只有N-1，最后异或N
       return res


