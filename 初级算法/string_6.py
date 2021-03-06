#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/37/
# 字符串转换整数 (atoi)
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。

# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

# 在任何情况下，若函数不能进行有效的转换时，请返回 0。

# 说明：

# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

# 示例 1:

# 输入: "42"
# 输出: 42
# 示例 2:

# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 示例 3:

# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 示例 4:

# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
# 示例 5:

# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
#      因此返回 INT_MIN (−231) 。
import math
class Solution(object):
    def myAtoi111(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = len(str)
        i=0
        m = ["0","1","2","3","4","5","6","7","8","9"]
        n = []
        while i<l:
            if str[i] not in m:
                ltmp = len(n)
                if ltmp == 0 and str[i]!=" ":
                    if str[i] in ["-","+"]:
                        n.append(str[i])
                        i+=1
                        continue
                    else:
                        return 0
                elif ltmp>=1:
                    break
                i+=1
                continue
            n.append(str[i])
            i+=1
        print(n)
        l2 = len(n)

        if n ==["-"] or l2==0:
            return 0

        # 这里可以直接用int(n[:])
        p=0
        r = 0
        for idx,i in enumerate(n):
            if i in ["-","+"]:
                continue
            r += int(i)*(10**(l2-idx-1))
        print(r)
        if n[0] =="-":
            r=0-r
        if r>2147483647:
            return 2147483647
        elif r< -2147483648:
            return -2147483648
        else:
            return r

    # 看这个
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s=s.lstrip()
        if len(s)==0:
            return 0
        #设置默认输出为0
        last=0
        #为了s[:i] ，如果有符号设置起始位置2，其余的为1
        i=2 if s[0]=='-'or s[0]=='+'  else 1
        #循环，直到无法强转成int，跳出循环
        while i <= len(s):
            try:
                last=int(s[:i])
                i+=1
            except:
                break#不是数字会出发异常
            print(last)
        if last<-2147483648 :
            return -2147483648
        if last>2147483647:
            return 2147483647
        return last

    def myAtoi2(self, s):
        import re 
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

    # 如果是+或者是-，并且是第一位，我们认为是合法的。
    # 剩下的迭代，只有在 ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]中，我们才认为合法
    # 最后如果res是+或者-，说明本身不合法，我们返回0。 否则我们迭代一次求出整数。这里为了简单直接使用了int函数
    def strToInt(self, s: str) -> int:
        cs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        res = ""
        s =  s.strip()
        for i in range(len(s)):
            c = s[i]
            if (c == '+' or c == '-') and i == 0:
                res += c
                continue
            if c not in cs: break
            res += c
        if res == '+' or res == '-': return 0
        return max(-2**31, int(res or 0)) if int(res or 0) < 0 else min(2**31 - 1, int(res or 0))

s = "42"
s = "   -42"
# s = "4193 with words"
# s = "words and 987"
# s = "-91283472332"
s = "+-2"
obj = Solution()
n = obj.myAtoi(s)
print('return', n)