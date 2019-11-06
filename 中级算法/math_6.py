#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/117/
# 两数相除
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。

# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 示例 2:

# 输入: dividend = 7, divisor = -3
# 输出: -2
# 说明:

# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

# https://blog.csdn.net/weixin_41958153/article/details/80797415
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #首先这一句就很python，postive 为true是符号相同
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        #检查dividend是否大于divisor
        #如果还小于则进行小精度的逼近dividend
        while dividend >= divisor:
            temp, i = divisor, 1
            #增大逼近dividend的步伐
            #i不断增加， temp不断减少
            while dividend >= temp:
                #经过上一句的判断，所以dividend还大于0
                dividend -= temp
                #商要加对应的i
                res += i
                #倍数相应的要增加
                i = i<<1
                #目前的值也要不断的增加
                temp = temp<<1
        #判定正负号
        if not positive:
            res = -res
        return min(max(-2147483648,res), 2147483647)

dividend = 10
divisor = 3
s = Solution()
n = s.divide(dividend, divisor)
print(n)









