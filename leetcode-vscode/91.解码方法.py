#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.20%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 167.3K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#

# @lc code=start
class Solution:
    # 动态规划
    # 跑到当前位的时候，不要判断当前位，而要判断前一位和前2位
    def numDecodings(self, s: str) -> int:
        if len(s)==0: return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            pre = int(s[i-1])                       
            if 1<=pre<=9:                           #前一位数1-9，dp[i]+dp[i-1]
                dp[i] += dp[i-1]
            if i>=2:
                pre = int(s[i-2])*10 + int(s[i-1])  #前2位组成两位数
                if 10<=pre<=26:
                    dp[i] += dp[i-2]                #dp当前+前2位
        return dp[-1]


# @lc code=end

s = "12"
# s = "226"
o = Solution()
print(o.numDecodings(s))