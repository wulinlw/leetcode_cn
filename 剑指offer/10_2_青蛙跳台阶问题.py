#!/usr/bin/python
#coding:utf-8

# 青蛙跳台阶问题
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


class Solution:
    def fabonacii(self,n):
        dp = [0,1]
        if n==0: return 0
        for i in range(n):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]
            
        
obj = Solution()
print(obj.fabonacii(0))
print(obj.fabonacii(1))
print(obj.fabonacii(5))