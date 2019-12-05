#!/usr/bin/python
# coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/54/
# 爬楼梯
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

    # 带缓存的递归
    def fib(self, N):
        cache = {}

        def recur_fib(N):
            if N in cache:
                return cache[N]
            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)
            # put result in cache for later reference.
            cache[N] = result
            return result

        return recur_fib(N)

    def climbStairs2(self, n):
        if(n == 1 or n == 0):
            return 1
        a, b = 1, 1  # 第0，1步都是1
        result = 0
        while(n > 1):
            result = a + b
            a, b = b, result
            n = n - 1
        return result

    def climbStairs3(self, n):
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # 打印出所有的走法
    def climbStairs4(self, n):
        lis = []
        # 0个2， 1个2，2个2 每次2步，看最多能几次
        # 所有的组合
        for i in range(n//2+1):
            twos = [2] * i
            ones = [1] * (n-2*i)
            lis.append(ones+twos)
        # print(lis)

        res = []
        # 每种步数全排列
        for i in lis:
            self.backtrack(i, [], res)
        return res

    # 有重复值的全排列
    # nums.sort()
    # self.backtrack(i, [], res)
    def backtrack(self, nums, tmp, res):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]], res)

    def climbStairs5(self, n):
        from copy import deepcopy
        re = []
        stack = []
        def climb(stack, n):
            if n == 0:
                tmp = deepcopy(stack)
                re.append(tmp)
                # print(stack)
            if n >= 1:
                stack.append(1)
                climb(stack, n-1)
                stack.pop()
            if n >= 2:
                stack.append(2)
                climb(stack, n-2)
                stack.pop()
        climb(stack,n)
        # print(re)
        return re


n = 4
s = Solution()
# re = s.climbStairs(n)
# print("deep:", re)

# re = s.climbStairs2(n)
# print("deep:", re)


n = 4
s = Solution()
re = s.climbStairs5( n)
print("deep:", re)
