# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.06.最小差
# 
# https://leetcode-cn.com/problems/smallest-difference-lcci/
# 
# 给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
# 示例：
# 输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# 输出： 3，即数值对(11, 8)
# 
# 提示：
# 
# 1 
# -2147483648 
# 正确结果在区间[-2147483648, 2147483647]内
# 
# 
# 
# Medium 39.1%
# Testcase Example: [0]
# [2147483647]
# 
# 提示:
# 如果你对数组排序呢?
# 考虑如何合并两个有序数组。
# 假设你把两个数组排序，然后遍历它们。如果第一个数组中的指针指向3，第二个数组中的指针指向9，那么移动第二个指针会对这一对数字的差产生什么影响?
# 
# 
from typing import List
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        l1, l2 = len(a), len(b)
        i, j = 0, 0
        re = float('inf')
        while i < l1 and j < l2:
            if a[i] == b[j]:
                return 0 
            elif a[i] < b[j]:
                re = min(re, b[j] - a[i])
                i += 1
            else:
                re = min(re, a[i] - b[j])
                j += 1
        return re


a = [1, 3, 15, 11, 2]
b = [23, 127, 235, 19, 8]
o = Solution()
print(o.smallestDifference(a, b))