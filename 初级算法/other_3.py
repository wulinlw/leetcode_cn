#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/66/
# 颠倒二进制位
# 颠倒给定的 32 位无符号整数的二进制位。

# 示例 1：
# 输入: 00000010100101000001111010011100
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
#       因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
# 示例 2：
# 输入：11111111111111111111111111111101
# 输出：10111111111111111111111111111111
# 解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
#       因此返回 3221225471 其二进制表示形式为 10101111110010110010011101101001。
 
# 提示：
# 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -1073741825。

# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # format语法a :[填充字符][对齐方式 <^>][宽度]
        print(bin(n))
        bits = "{:0>32b}".format(n)
        print(bits)
        return int(bits[::-1], 2)#2进制

    def reverseBits2(self, n):
        res = 0
        count = 32
        
        while count:
            res <<= 1
            # 取出 n 的最低位数加到 res 中
            res += n&1
            n >>= 1
            count -= 1
            
        return int(bin(res), 2)

        
    def reverseBits3(self, n):
        c=32
        re = 0
        while c>0:
            if n&1 ==1:
                tmp = 1<<(c-1)
                re = re^tmp
            n=n>>1
            c-=1
        return re

n=213
s = Solution()
re = s.reverseBits(n)
print("deep:","{:0>32b}".format(re))