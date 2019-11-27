#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/201/two-pointer-technique/785/
# 两数之和 II - 输入有序数组
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 说明:

# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 定义low，high指针分别处在数组两端 
        low,high = 0,len(numbers) - 1
        while low < high:
            # 如果两指针之和为target值，返回索引+1
            if numbers[low] + numbers[high] == target:
                return low + 1,high + 1
            # 如果两指针指向值之和大于target值，high指针左移
            elif numbers[low] + numbers[high] > target:
                high -= 1
            # 如果两指针指向值之和小于target值，low指针右移
            else:
                low += 1



numbers = [2, 7, 11, 15]
target = 9
s = Solution()
n = s.twoSum(numbers, target)
print(n)       