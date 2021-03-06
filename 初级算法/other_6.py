#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/69/
# 缺失数字
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

# 示例 1:
# 输入: [3,0,1]
# 输出: 2

# 示例 2:
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #总合-列表之和
        #1到n之和，(n*(n+1))/2
        l = len(nums)
        return(int(l*(l+1)/2)-sum(nums))

    def missingNumber2(self, nums):
        num_set = set(nums)
        print(num_set)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number



n=[3,0,1]
s = Solution()
re = s.missingNumber2(n)
print("deep:",re)