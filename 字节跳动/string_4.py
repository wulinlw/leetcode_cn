#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1015/
# 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 示例 1:
# 输入: num1 = "2", num2 = "3"
# 输出: "6"

# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：

# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 每一位相乘，结果放入数组，然后相加
        #把num1,num2翻转方便计算
        num1 = num1[::-1]; num2 = num2[::-1]
        #每一位互相乘的结果用一维数组去储存
        arr = [0 for i in range(len(num1)+len(num2))]
        #填充这个一维数组
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])
                print(arr)
        ans = []
        #计算每一位的终极结果
        for i in range(len(arr)):
            #digit表示这一位的数字
            digit = arr[i] % 10
            #carry表示加给下一位的量
            carry = arr[i] // 10
            if i < len(arr)-1:
                #下一位加上
                arr[i+1] += carry
            #更新答案
            ans.insert(0, str(digit))
        #去除首位为0的情况
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        #连接成字符串
        return ''.join(ans)


num1 = "12"
num2 = "34"
s = Solution()
n = s.multiply(num1, num2)
print(n)