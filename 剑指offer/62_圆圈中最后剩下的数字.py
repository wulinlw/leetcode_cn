#!/usr/bin/python
#coding:utf-8

# // 面试题62：圆圈中最后剩下的数字
# // 题目：0, 1, …, n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里
# // 删除第m个数字。求出这个圆圈里剩下的最后一个数字。
class Solution(object):
    # 也可以用链表，循环即可
    def LastRemaining_1(self, n, m):
        if n<0 or m<0:return False
        nums = [i for i in range(n)]
        index = 0                       #要删除的索引
        while len(nums)>1:
            index = (m+index-1)%len(nums)
            nums.pop(index)
        return nums[0]

    def LastRemaining_2(self, n, m):
        if n<0 or m<0:return False
        last = 0 
        for i in range(2, n+1):
            last = (last+m)%i
        return last


n = 9
m = 13
S = Solution()
print(S.LastRemaining_1(n, m))
print(S.LastRemaining_2(n, m))
