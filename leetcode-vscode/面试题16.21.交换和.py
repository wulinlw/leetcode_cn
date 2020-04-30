# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.21.交换和
# 
# https://leetcode-cn.com/problems/sum-swap-lcci/
# 
# 给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
# 返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
# 
# 示例:
# 
# 输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
# 输出: [1, 3]
# 
# 
# 示例:
# 
# 输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
# 输出: []
# 
# 提示：
# 
# 
# 	1 <= array1.length, array2.length <= 100000
# 
# 
# 
# Medium 43.6%
# Testcase Example: [4, 1, 2, 1, 1, 2]
# [3, 6, 3, 3]
# 
# 提示:
# 在这里用一些例子做些数学计算。这一对数值有什么需求？你发现它们的值有什么特点？
# 当你把一个值a从数组A移动到数组B时，A的和减少了a, B的和增加了a。当你交换两个值时会发生什么？交换两个值并得到相同的和需要什么？
# 如果你交换两个值，即a和b，那么A的和变成sumA - a + b，而B的和变成sumB - b + a。这两个和需要相等。
# 你在寻找a和b的值，其中sumA - a + b = sumB - b + a。用数学方法算出这对a和b的值意味着什么。
# 如果计算一下，那我们要找一对这样的值，即a - b = (sumA - sumB) / 2。然后，问题归结为寻找具有特定差的一对值。
# 一种蛮力解法是遍历所有的数值对，以找到一个具有正确差值的数值对。这可能看起来为：对A进行外循环，对B进行内循环。对于每个值，计算差值并与目标差值进行比较。能说得更具体些吗？给定A中的值和目标差，可以知道要找的B中的元素的确切值吗?
# 蛮力解法其实是在B中寻找一个等于a - target的值。你如何能更快地找到这个元素？什么方法可以帮助我们快速找到数组中是否存在某个元素?
# 可以用散列表，也可以尝试排序。两者都能帮助我们更快地定位元素。
# 如果A的和是11，B的和是8呢？能有一对数刚好有目标差吗？检查你的解决方案是否恰当地处理了这种情况。
# 
# 
from typing import List
class Solution:
    # 先求两个数组的差值diff = sum(a)-sum(b), 如果为奇数直接return [], 因为交换任何数得到的diff一定是两个数字差值的2倍
    # 然后将数组b作为集合, 遍历数组a, 判断其每个元素-diff//2是否在b集合中, 在的话即为所求
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        diff = sum(array1) - sum(array2)
        if diff & 1:return []           #差是奇数，不可能平分到2个数组
        diff >>= 1                       #除以2
        s2 = set(array2)                #去重
        for a in array1:                #在array1中找-diff//2, 即array1，array2中都有diff//2
            if a - diff in s2:
                return [a, a - diff]
        return []




array1 = [4, 1, 2, 1, 1, 2]
array2 = [3, 6, 3, 3]
o = Solution()
print(o.findSwapValues(array1, array2))