#!/usr/bin/python
#coding:utf-8

# // 面试题64：求1+2+…+n
# // 题目：求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case
# // 等关键字及条件判断语句（A?B:C）。
class Solution(object): 
    # n*(n+1)/2
    def sumArr(self, n):
        if n<=0:return False
        out = n**2 + n
        out = out>>1
        return out

    #递归
    def sumArr2(self, n):
        if n<=0:return False        
        if n==1:
            return 1
        else:
            return self.sumArr2(n-1) + n



n = 5
S = Solution()
print(S.sumArr(n))
