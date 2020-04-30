# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.24.数对和
# 
# https://leetcode-cn.com/problems/pairs-with-sum-lcci/
# 
# 设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
# 示例 1:
# 
# 输入: nums = [5,6,5], target = 11
# 输出: [[5,6]]
# 
# 示例 2:
# 
# 输入: nums = [5,6,5,6], target = 11
# 输出: [[5,6],[5,6]]
# 
# 提示：
# 
# 
# 	nums.length <= 100000
# 
# 
# 
# Medium 47.0%
# Testcase Example: [5]
# 1
# 
# 提示:
# 从蛮力解法开始。运行复杂度是什么？解决这个问题的最佳时间是什么？
# 我们可以用散列表使它更快吗?
# 如果数组有序呢？
# 如果我们对数组进行排序，那么就可以对数字进行重复的二进制搜索。如果数组是有序的呢？我们能否在O(N)时间和O(1)空间中求解这个问题？
# 
# 
from typing import List
class Solution:
    # 存储每个数组元素i出现的次数，
    # 若target-i出现过，就一起放入返回容器中，并将target-i出现的次数减1
    # 否则将i出现的次数加1
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        re = []
        m = {}
        for i in nums:
            m[target-i] = m.get(target-i, 0)
            if m[target-i] > 0:
                m[target-i] -= 1
                re.append([i, target-i])
            else:
                m[i] = m.get(i, 0) + 1
        return re


nums = [5,6,5]
target = 11
o = Solution()
print(o.pairSums(nums, target))