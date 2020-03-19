#!/usr/bin/python
#coding:utf-8

# 面试题 08.04. 幂集
# 幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

# 说明：解集不能包含重复的子集。

# 示例:

#  输入： nums = [1,2,3]
#  输出：
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# https://leetcode-cn.com/problems/power-set-lcci/


from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        re = []
        def backtrack(nums, idx, tmp):
            re.append(tmp[:])
            for i in range(idx, len(nums)):     #这里是从idx开始
                tmp.append(nums[i])
                backtrack(nums, i+1, tmp)   #从i+1
                tmp.pop()
        backtrack(nums, 0, [])
        return re

nums = [1,2,3]
o = Solution()
print(o.subsets(nums))