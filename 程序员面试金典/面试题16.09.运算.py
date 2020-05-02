# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.09.运算
# 
# https://leetcode-cn.com/problems/operations-lcci/
# 
# 请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。
# 你的实现应该支持如下操作：
# 
# Operations() 构造函数
# minus(a, b) 减法，返回a - b
# multiply(a, b) 乘法，返回a * b
# divide(a, b) 除法，返回a / b
# 
# 示例：
# Operations operations = new Operations();
# operations.minus(1, 2); //返回-1
# operations.multiply(3, 4); //返回12
# operations.divide(5, -2); //返回-2
# 
# 提示：
# 
# 你可以假设函数输入一定是有效的，例如不会出现除法分母为0的情况
# 单个用例的函数调用次数不会超过1000次
# 
# 
# 
# Medium 45.2%
# Testcase Example: ["Operations","minus","minus","multiply","multiply","divide","divide"]
# [[],[0,-2147483647],[-1,2147483647],[-1,-2147483647],[-100,21474836],[2147483647,-1],[-2147483648,1]]
# 
# 提示:
# 从减法开始，逐步解决。一旦完成了一个函数，你可以用它来实现其他函数。
# 减法：取负函数（将正整数转换为负数）有用吗？你可以使用加法操作符来实现吗?
# 当a > b时，a – b > 0。你能得到a – b的符号位吗？
# 你考虑过如何处理a – b中的整数溢出吗？
# 
# 
# https://leetcode-cn.com/problems/operations-lcci/solution/tong-guo-er-fen-de-xing-shi-shi-xian-cheng-chu-fa-/
class Operations:

    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        return a + (~b) + 1                     #补码加法

    def multiply(self, a: int, b: int) -> int:
        #处理符号
        sign = True
        if a < 0:
            sign = not sign
            a = -a
        if b < 0:
            sign = not sign
            b = -b
        #用较小的数做乘数
        if a < b:
            a, b = b, a

        #循环每一轮做分解， `a * b = (a * 2) * (b // 2) + a * (b % 2)`
        remainder = 0
        while b > 1:
            #b = b // 2, r = b % 1
            b, r = self.divideBy2(b)
            if r == 1:
                remainder = remainder + a
            a = a + a
        a = a + remainder

        if sign:
            return a
        return -a
    
    # 求num//2，返回商和余数
    def divideBy2(self, num)-> (int, int): 
        res = 0
        while res < self.minus(num, res):
            half = 1
            while True:
                if res + half + half < self.minus(num, (res + half + half)):
                    half = half + half
                else:
                    break
            res = res + half
        if res == self.minus(num, res):
            return (res, 0)
        else:
            return (self.minus(res, 1), 1)

    # 第29题
    def divide(self, a: int, b: int) -> int:
        sign = True
        if a < 0:
            sign =  not sign
            a = -a
        if b < 0:
            sign = not sign
            b = -b
        ans = 0
        while a >= b:
            divisor = b
            cnt = 1
            while divisor + divisor < a:
                divisor = divisor + divisor
                cnt = cnt + cnt
            a = self.minus(a, divisor)
            ans = ans + cnt
        if not sign:
            return -ans
        return ans

# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)



