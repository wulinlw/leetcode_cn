#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (56.45%)
# Likes:    592
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 62.7K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 示例 1:
# 
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释: 
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2:
# 
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释: 
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
#

# @lc code=start
class Solution:
    # dp[i][j]表示s1[0..i] 和 s2[0..j]的最小编辑距离
    # dp[i][j] = min(
    #     dp[i-1][j-1],     #替换，跳过 左上
    #     dp[i][j-1],       #插入      左方
    #     dp[i-1][j],       #删除      上方
    # )   
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for i in range(l2+1)] for i in range(l1+1)]
        
        for i in range(1, l1+1):                #第一列
            dp[i][0] = i
        for i in range(1, l2+1):                #第一行
            dp[0][i] = i
        for i in range(1,l1+1):
            for j in range(1, l2+1):
                if word1[i-1]==word2[j-1]:      #为什么-1，因为如果对比的2个字符相等，就上面都不需要做，直接取左上方的值即可，即左上方值相等
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
        return dp[-1][-1]

# @lc code=end

word1 = "horse"
word2 = "ros"
o = Solution()
print(o.minDistance(word1, word2))