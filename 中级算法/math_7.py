#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/118/
# 分数到小数
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
# 如果小数部分为循环小数，则将循环的部分括在括号内。

# 示例 1:
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 示例 2:

# 输入: numerator = 2, denominator = 1
# 输出: "2"
# 示例 3:

# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"

# https://blog.csdn.net/weixin_41011942/article/details/86725429
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        elif denominator == 0:
            return ''
        else:
            isNegative = (numerator < 0) ^ (denominator < 0)
            numerator = abs(numerator)
            denominator = abs(denominator)
            res = ''
            res += '-' if isNegative else ''
            res += str(numerator//denominator)#取整数位
            numerator %= denominator#取小数位
            if numerator == 0:
                return res
            else:
                res +='.'
                dic = {}#用于判断循环的字典
                # print(numerator)
                while numerator:
                    if numerator in dic:
                        start = dic[numerator]
                        end = len(res)
                        res = res[:start] + '(' + res[start:end] + ')'
                        return res
                    dic[numerator] = len(res)
                    res += str(numerator*10//denominator)
                    numerator = numerator*10%denominator
                    # print(dic,res,numerator)
                return res


numerator = 2
denominator = 7
s = Solution()
n = s.fractionToDecimal(numerator, denominator)
print(n)









