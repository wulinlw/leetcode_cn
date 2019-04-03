#!/usr/bin/python
#coding:utf-8

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

# 爬楼梯问题的实质就是 斐波那契数列
# f(n) = f(n-1) + f(n-2)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 1 or n == 0):
            return 1
        else:
            # 假如不是以类的形式, 直接 return 函数() 不需要加 self.
            return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairs2(self, n):
        if(n == 1 or n == 0):
            return 1
        a, b = 1, 1
        result = 0
        while(n > 1):
            result = a + b
            a, b = b, result
            n = n - 1
        return result
        

n = 7
s = Solution()
re = s.climbStairs(n)
print("deep:",re)

re = s.climbStairs2(n)
print("deep:",re)
