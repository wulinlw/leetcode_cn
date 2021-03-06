# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题05.07.配对交换
# 
# https://leetcode-cn.com/problems/exchange-lcci/
# 
# 配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。
#  示例1:
# 
# 
#  输入：num = 2（或者0b10）
#  输出 1 (或者 0b01)
# 
# 
#  示例2:
# 
# 
#  输入：num = 3
#  输出：3
# 
# 
#  提示:
# 
# 
# num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。
# 
# 
# 
# Easy 67.9%
# Testcase Example: 3
# 
# 提示:
# 交换每一对意味着把偶数位移到左边，奇数位移到右边。你能把这个问题分成几个部分吗？
# 你能创建一个代表偶数位的数字吗？那么你可以将偶数位移过一位吗？
# 二进制的1010等价于十进制的10，也相当于十六进制的0xA。那么二进制的101010...在十六进制中是什么？也就是说，你要如何表示1在奇数位上的1和0交替序列？如果反过来呢（1在偶数位）？
# 尝试用掩码0xaaaaaaaa和0x55555555提取偶数位和奇数位。然后尝试移动偶数位和奇数位来创建正确的数字。
# 
# 

class Solution:
    # 对于奇数位，使用 101010（即 0xAA）作为掩码，提取奇数位，并把它们右移一位；
    # 对于偶数位，使用 010101（即 0x55）作为掩码，提取偶数位，并把它们左移一位。
    def exchangeBits(self, num: int) -> int:
        return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)

num = 2 
o = Solution()
print(o.exchangeBits(num))