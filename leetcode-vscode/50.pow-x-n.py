#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (34.01%)
# Likes:    353
# Dislikes: 0
# Total Accepted:    82.4K
# Total Submissions: 233K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 
#

# @lc code=start
class Solution:
    def myPow1(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow1(x, -n)
        elif n % 2 == 0 :
            return self.myPow1(x*x,n//2)
        else:
            return self.myPow1(x*x,(n-1)//2)*x
    
    def myPow2(self, base: float, exponent: int) -> float:
        if exponent==0: return 1
        if exponent==1: return base
        if exponent<0:return 1/self.myPow2(base, -exponent)
        re = self.myPow2(base, exponent>>1)
        re *= re
        if exponent & 1 == 1:#奇数，需要乘以自己
            re *= base
        return re

    def myPow3(self, x: float, n: int) -> float:
        def quick(N):
            if N == 0: return 1
            re = quick(N//2)
            return re*re if N%2==0 else re*re*x

        return quick(n) if n >= 0 else 1/quick(-n)

    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

        
# @lc code=end

o = Solution()
print(o.myPow3(2, 10))
print(o.myPow3(2.1, 3))
print(o.myPow3(2, -2))