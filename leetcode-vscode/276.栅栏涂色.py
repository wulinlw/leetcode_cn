#
# @lc app=leetcode.cn id=276 lang=python3
#
# [276] 栅栏涂色
#
# https://leetcode-cn.com/problems/paint-fence


# 有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。
# 你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。

# 注意:
# n 和 k 均为非负的整数。

# 示例:
# 输入: n = 3，k = 2
# 输出: 6
# 解析: 用 c1 表示颜色 1，c2 表示颜色 2，所有可能的涂色方案有:

#             柱 1    柱 2   柱 3     
#  -----      -----  -----  -----       
#    1         c1     c1     c2 
#    2         c1     c2     c1 
#    3         c1     c2     c2 
#    4         c2     c1     c1  
#    5         c2     c1     c2
#    6         c2     c2     c1

class Solution:
    # i与i-1颜色相同，则i-2的涂色方案为F(i-2)，当前栅栏的涂色方式有k-1种。
    # i与i-1颜色不同，当前栅栏颜色涂色方式有k-1种
    # F(i)=F(i-2)*k-1 + F(i-1)*k-1
    # dp[0], dp[1], dp[2] = 0, k, k * k     解释如下
    # dp[1] 第一个k种
    # dp[2] 第一个k种，第二个相同时位k，不同时k*(k-1) ,总共是k+k*(k-1)=k*k
    def numWays(self, n: int, k: int) -> int:
        dp = [0] * (n + 3)                                      #防止n长度不够溢出
        dp[0], dp[1], dp[2] = 0, k, k * k
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
        return dp[n]



n = 3
k = 2
o = Solution()
print(o.numWays(n, k))