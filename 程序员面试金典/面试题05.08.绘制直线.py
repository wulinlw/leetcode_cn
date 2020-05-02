# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题05.08.绘制直线
# 
# https://leetcode-cn.com/problems/draw-line-lcci/
# 
# 绘制直线。有个单色屏幕存储在一个一维数组中，使得32个连续像素可以存放在一个 int 里。屏幕宽度为w，且w可被32整除（即一个 int 不会分布在两行上），屏幕高度可由数组长度及屏幕宽度推算得出。请实现一个函数，绘制从点(x1, y)到点(x2, y)的水平线。
# 给出数组的长度 length，宽度 w（以比特为单位）、直线开始位置 x1（比特为单位）、直线结束位置 x2（比特为单位）、直线所在行数&nbsp;y。返回绘制过后的数组。
# 
# 示例1:
# 
#  输入：length = 1, w = 32, x1 = 30, x2 = 31, y = 0
#  输出：[3]
#  说明：在第0行的第30位到第31为画一条直线，屏幕表示为[0b000000000000000000000000000000011]
# 
# 
# 示例2:
# 
#  输入：length = 3, w = 96, x1 = 0, x2 = 95, y = 0
#  输出：[-1, -1, -1]
# 
# 
# 
# Medium 54.6%
# Testcase Example: 1
# 32
# 30
# 31
# 0
# 
# 提示:
# 先试试简单解法。你能设置一个特定的“像素”吗？
# 当你画一条长线时，你会得到即将变成1的序列的全部字节。你可以一次性设置它吗？
# 那这条线的起点和终点呢？你需要单独设置这些像素，还是可以同时设置所有像素？
# 当x1和x2在同一个字节中时，你的代码能否处理这种情况。
# 
# 
from typing import List
class Solution:
    # length是返回数组的大小，每一个值是int， 对应32位，32个像素.
    # 二维转一维, (x,y)坐标 对应 length的二进制数组.
    # 二维屏幕的宽度是w位，高是多少不用关心，关心的是第y行之前已经有多少个位了，这个偏移量对应到length数组里就是 y*w/32
    # 然后就可以画线了
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        re = [0] * length
        for i in range(x1,x2+1):
            re[y*(w//32) + i//32] |= 1<<(31-i%32)
        return re

    def drawLine2(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        l = list()
        num = length * 32
        martix = ['0'] * num
        for idx in range(x1, x2+1):
            martix[w*y+idx] = '1'
        for idx in range(0, num, 32):
            num = int(''.join(martix[idx:idx+32]),2)
            num &= 0xFFFFFFFF
            if ((num & 0x80000000)>>31) == 1:
                num = ~(num ^ 0xFFFFFFFF)
            l.append(num)
        return l

length = 1
w = 32
x1 = 30
x2 = 31
y = 0
o = Solution()
print(o.drawLine(length, w, x1, x2, y))