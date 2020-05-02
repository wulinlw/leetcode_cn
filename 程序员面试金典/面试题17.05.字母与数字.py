# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.05. 字母与数字
# 
# https://leetcode-cn.com/problems/find-longest-subarray-lcci/
# 
# 给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。
# 返回该子数组，若存在多个最长子数组，返回左端点最小的。若不存在这样的数组，返回一个空数组。
# 
# 示例 1:
# 
# 输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
# 
# 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
# 
# 
# 示例 2:
# 
# 输入: ["A","A"]
# 
# 输出: []
# 
# 
# 提示：
# 
# 
# 	array.length <= 100000
# 
# 
# 
# Medium 33.9%
# Testcase Example: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
# 
# 提示:
# 是哪个字母或数字并不重要。你可以把该问题简化为只包含 A 和 B 的数组。然后寻找具有相同数量的 A 和 B 的最长子数组。
# 从蛮力解法开始。
# 如果你从一开始就计算 A 的个数和 B 的个数会怎样(试着构建数组构成的表并保存到目前为止 A 和 B 的数量)?
# 当表中 A 和 B 的个数相等时，整个子数组(从索引 0 开始)的 A 和 B 的个数相等。如何使用该表来查找不以索引 0 开始的、符合条件的子数组?
# 假设在这个表中，索引 i 满足 count(A, 0->i) = 3 和 count(B, 0->i) = 7。这意味着 B 比 A 多 4 个。如果你发现后面的某点 j 具有相同的差值(count(B, 0->j) - count(a, 0->j))，那么这表示子数组中有相同数量的 A 和 B。
# 
# 
from typing import List
class Solution:
    # 前缀和
    # 将数字和字母转为1、-1，re字典记录下前n项和的值（sum）及第一个下标的位置，如果最后的结果为前m项和值为0,表示前面m项就是题目要求。
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        dic = {0:-1}
        sum = 0                                 #前缀和
        maxlen = 0 
        left, right = 0,0 
        for idx,s in enumerate(array):
            if s.isalpha():                     #字母+1， 数字-1
                sum += 1
            else:
                sum -= 1
            if sum not in dic:                  #记录前缀和第一次出现的位置
                dic[sum] = idx
            else:
                if idx - dic[sum] > maxlen:     #找到更长的，更新下maxlen，idx - dic[sum] 当前位置 - 这个前缀和第一次出现的位置
                    maxlen = idx - dic[sum]
                    left = dic[sum] + 1         #左边界不包含，第一次出现的位置+1，
                    right = idx + 1             #包含右边界+1
        return array[left:right]

array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
o = Solution()
print(o.findLongestSubarray(array))
