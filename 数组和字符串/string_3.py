#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/200/introduction-to-string/779/
# 二进制求和
# 给定两个二进制字符串，返回他们的和（用二进制表示）。

# 输入为非空字符串且只包含数字 1 和 0。
# 示例 1:

# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:

# 输入: a = "1010", b = "1011"
# 输出: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r, p = '', 0#p是进位
        #用0补齐短的二进制数
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        # print(a,b)
        for i, j in zip(a[::-1], b[::-1]):
            # print(i,j)
            s = int(i) + int(j) + p#加起来的值，p是进位的
            p = s // 2#s=2的时候进位
            r = str(s % 2) + r#结果存储，str(s % 2)是当前的0或1，是1就是没进位，是2就当前为0，进位1
            # print(s,r,p)
        return '1' + r if p else r

a = "11"
b = "1"
s = Solution()
n = s.addBinary(a,b)
print(n)       