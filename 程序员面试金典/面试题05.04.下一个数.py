# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题05.04.下一个数
# 
# https://leetcode-cn.com/problems/closed-number-lcci/
# 
# 下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。
#  示例1:
# 
# 
#  输入：num = 2（或者0b10）
#  输出：[4, 1] 或者（[0b100, 0b1]）
# 
# 
#  示例2:
# 
# 
#  输入：num = 1
#  输出：[2, -1]
# 
# 
#  提示:
# 
# 
# num的范围在[1, 2147483647]之间；
# 如果找不到前一个或者后一个满足条件的正数，那么输出 -1。
# 
# 
# 
# Medium 39.5%
# Testcase Example: 2
# 
# 提示:
# 下一步：从每个蛮力解法开始。
# 下一个：想象一个二进制数，在整个数中分布一串1和0。假设你把一个1翻转成0，把一个0翻转成1。在什么情况下数会更大？在什么情况下数会更小？
# 下一步：如果你将1翻转成0，0翻转成1，假设 0 -> 1位更大，那么它就会变大。你如何使用这个来创建下一个最大的数字（具有相同数量的1）？
# 下一步：你能翻转0到1，创建下一个最大的数字吗？
# 下一步：把0翻转为1将创建一个更大的数字。索引越靠右，数字越大。如果有一个1001这样的数字，那么我们就想翻转最右边的0（创建1011）。但是如果有一个1010这样的数字，我们就不应该翻转最右边的1。
# 下一步：我们应该翻转最右边但非拖尾的0。数字1010会变成1110。完成后，我们需要把1翻转成0让数字尽可能小，但要大于原始数字（1010）。该怎么办？如何缩小数字？
# 下一步：我们可以通过将所有的1移动到翻转位的右侧，并尽可能地向右移动来缩小数字（在这个过程中去掉一个1）。
# 获取前一个：一旦你解决了“获取后一个”，请尝试翻转“获取前一个”的逻辑。
# 
# 
from typing import List
class Solution:
    # 比 num 大的数：从右往左，找到第一个 01 位置，然后把 01 转为 10，右侧剩下的 1 移到右侧的低位，右侧剩下的位清0。
    # 比 num 小的数：从右往左，找到第一个 10 位置，然后把 10 转为 01，右侧剩下的 1 移到右侧的高位，右侧剩下的位置0。
    # https://leetcode-cn.com/problems/closed-number-lcci/solution/wei-yun-suan-by-suibianfahui/
    def findClosedNumbers(self, num: int) -> List[int]:
        mn, mx = 1, 2147483647

        def findLarge(n):
            # 从右开始找到第1个1
            # 然后记录1的个数ones直到再遇到0或到最高位
            # 然后将这个0变成1
            # 然后右边的位数用000...111(ones-1个1)填充
            checkMask = 1
            bits = 0
            while checkMask <= n and checkMask & n == 0:            #找到左边第一个1为止
                checkMask <<= 1
                bits += 1                                           #右边0的个数
            ones = 0  
            while checkMask <= n and checkMask & n != 0:            #找到第一个0
                ones = (ones << 1) + 1                              #左边1的个数
                checkMask <<= 1
                bits += 1                                           #找到01，一共左移了多少位，
            ones >>= 1                                              #因为ones初始化为1, 所以ones需要右移一位
            n |= checkMask                                          #01变10
            # print("{:0>32b}".format(n))
            n = (n >> bits) << bits                                 #右边都变成0了
            n |= ones                                               #将右边填充上ones
            return n if mn <= n <= mx else -1

        def findSmall(n):
            # 从右开始找到第1个0, 记录此过程1的个数ones
            # 然后继续往左找直到再遇到1
            # 然后将这个1变成0, ones也要左移一位(也可以初始化为1)
            # 然后右边的位数用高位ones个1填充, 即构造出111...000, 可以直接基于ones构造
            # 注意如果全为1的话是无解的, 直接返回-1
            checkMask = 1
            bits = 0
            ones = 1
            while checkMask <= n and checkMask & n != 0:            #找到第一个0
                checkMask <<= 1
                bits += 1
                ones = (ones << 1) + 1                              #记录有多少1
            if checkMask > n:
                # 全部是1
                return -1
            while checkMask <= n and checkMask & n == 0:            #在找第一个1
                checkMask <<= 1
                bits += 1
                ones <<= 1
            # print("{:0>32b}".format(ones))
            ones >>= 1                                              #因为ones初始化为1, 所以ones需要右移一位
            n &= ~checkMask                                         #10变01
            n = (n >> bits) << bits                                 #右边都变成0了
            n |= ones                                               #将右边填充上ones
            return n if mn <= n <= mx else -1

        return [findLarge(num), findSmall(num)]



o = Solution()
print(o.findClosedNumbers(2))