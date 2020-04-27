# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.05.阶乘尾数
# 
# https://leetcode-cn.com/problems/factorial-zeros-lcci/
# 
# 设计一个算法，算出 n 阶乘有多少个尾随零。
# 示例 1:
# 
# 输入: 3
# 输出: 0
# 解释:&nbsp;3! = 6, 尾数中没有零。
# 
# 示例&nbsp;2:
# 
# 输入: 5
# 输出: 1
# 解释:&nbsp;5! = 120, 尾数中有 1 个零.
# 
# 说明: 你算法的时间复杂度应为&nbsp;O(log&nbsp;n)&nbsp;。
# 
# 
# Easy 46.2%
# Testcase Example: 3
# 
# 提示:
# 0如何变成n!？这是什么意思？
# n!中的每个0表示n能被10整除一次。这是什么意思？
# n!中每一个因子10都意味着n!能被5和2整除。
# 你能计算出5和2的因数的个数吗？需要两者都计算吗？
# 你是否考虑过25实际上记录了两次因数5？
# 
# 

class Solution:
    # 末尾的0都是2*5来的，统计有多少个5即可
    def trailingZeroes(self, n: int) -> int:
        m5 = 0
        while n>0:
            n //= 5
            m5 += n
        return m5

n = 5
o = Solution()
print(o.trailingZeroes(n))