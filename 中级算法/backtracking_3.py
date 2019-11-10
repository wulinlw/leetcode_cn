#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/93/
# 全排列
# 给定一个没有重复数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


# 我们举个例子，以字符串列表['a', 'b', 'c']为例，我们逐个位确定全排列的所有可能。回溯法的原理在于在前n-1位元素确定的情况下，求取n位以后的全排列。本例中，首先固定第0位，就是分别将第0位与它本身及后面各位元素交换，得到3种不同的可能，在固定这一位后，在考虑第1位的可能性，将第1位与它本身及其后元素交换，有两种可能性，当前两位元素确定后，最后一位只有一种可能性。因此一共有6种可能。
# 将列表的第0位与第0位交换（相当于不变），此时列表变为['a', 'b', 'c']；
# 1.1 将列表的第1位与第1位交换（相当于不变），得到列表['a', 'b', 'c']；
# 1.2 将列表的第1位与第2位交换，得到列表['a', 'c', 'b']；

# 将列表的第0位与第1位交换，得到列表['b', 'a', 'c']；
# 2.1 将列表的第1位与第1位交换（相当于不变），得到列表['b', 'a', 'c']；
# 2.2 将列表的第1位与第2位交换，得到列表['b', 'c', 'a']；

# 将列表的第0位与第2位交换，得到列表['c', 'b', 'a']；
# 3.1 将列表的第1位与第1位交换（相当于不变），得到列表['c', 'b', 'a']；
# 3.2 将列表的第1位与第2位交换，得到列表['c', 'a', 'b']

# 这里需要注意的是，每次交换元素并回溯寻找后，都要将元素交换回来，保持没有交换前的状态。

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        self.helper(nums,0)
        return self.res

    def helper(self,nums,i):
        nums1=nums[:]
        if i == (len(nums1)-1):
            self.res.append(nums1)
            return
        for l in range(i,len(nums)):
            nums1[i],nums1[l]=nums1[l],nums1[i]
            self.helper(nums1,i+1)
            nums1[i],nums1[l]=nums1[l],nums1[i]#交换回来



        

nums = [1,2,3]
s = Solution()
r = s.permute(nums)
print(r)




