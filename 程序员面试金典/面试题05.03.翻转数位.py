# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题05.03.翻转数位
# 
# https://leetcode-cn.com/problems/reverse-bits-lcci/
# 
# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
# 示例 1：
# 
# 输入: num = 1775(110111011112)
# 输出: 8
# 
# 
# 示例 2：
# 
# 输入: num = 7(01112)
# 输出: 4
# 
# 
# 
# Easy 46.9%
# Testcase Example: 0
# 
# 提示:
# 先试试蛮力解法。你能尝试一切可能性吗？
# 把0翻转到1可以合并两个1 的序列，但只有在这两个序列仅被一个0分隔时才可以。
# 每个序列都可以通过与邻近的序列合并或者直接翻转紧挨着的0来增加其长度。你只需要找到最好的选择。
# 尝试用线性时间、单次扫描和O(1) 空间完成它。
# 
# 

class Solution:
    def reverseBits(self, num: int) -> int:
        max = 0                             #记录最大长度
        cnt = 0                             #记录当前连续的1
        cntPre = 0                          #记录上一次连续的1
        while num:
            if 1 & num:                     #最后一位是1，cnt+1
                cnt += 1
            else:                           #碰到0，看看当前+上一个+1（当前的0）有没有破纪录
                if cntPre + cnt + 1 > max:
                    max = cntPre + cnt + 1
                cntPre = cnt                #重新计算cnt， cntPre
                cnt = 0
            num >>= 1                       #右移
        if cntPre + cnt + 1 > max:          #跳出循环后，还需要做一次判断，以应对“0”，“1111”等这种需要最高位左边再加一个1的情况。
            max = cntPre + cnt + 1
        return max


num = 1775
o = Solution()
print(o.reverseBits(num))