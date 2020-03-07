#!/usr/bin/python
#coding:utf-8

# // 面试题57（二）：和为s的连续正数序列
# // 题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
# // 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、
# // 4～6和7～8。


class Solution:
    # 双指针
    def FindContinuousSequence(self, target):
        i = j = 1
        res = []
        cur_sum = 0
        while j < target:
            cur_sum += j
            j += 1
            while cur_sum > target:
                cur_sum -= i
                i += 1
            if cur_sum == target:
                res.append(list(range(i, j)))
        return res


        
n = 18
obj = Solution()
print(obj.FindContinuousSequence(n))
