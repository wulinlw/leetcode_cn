#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (38.89%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 28.8K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 
# 示例 1:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false
# 
#

# @lc code=start
class Solution:
    # https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2 != len3): return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True                                           #都是空，True
        for i in range(1,len1+1):                               #第一列，上面true，且s1[i-1]==s3[i-1] 0-i是匹配的
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):                               #第一行，左边true，0-i是匹配的
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):                           #s1前i位，s2前j位，能组成s3的i+j位
                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
                            #dp[i][j-1]             s1的前i位，s2的前j-1位，可以组成s3的i+j-1位
                            #s2[j-1]==s3[i+j-1]     s2的j-1位字符，与s3的i+j-1位相同
                            #dp[i-1][j]             s1的前i-1位，s2的前j位，可以组成s3的i+j-1位
                            #s1[i-1]==s3[i+j-1]     s1的i-1位字符，与s3的i+j-1位相同
        return dp[-1][-1]

# @lc code=end

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

s1 = ""
s2 = ""
s3 = "a"

# s1 = "a"
# s2 = ""
# s3 = "a"
o = Solution()
print(o.isInterleave(s1, s2, s3))