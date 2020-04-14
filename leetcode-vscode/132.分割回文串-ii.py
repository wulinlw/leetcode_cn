#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (42.19%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 22K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回符合要求的最少分割次数。
# 
# 示例:
# 
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
#

# @lc code=start
class Solution:
    # dp[i]：表示前缀子串 s[0:i] 分割成若干个回文子串所需要最小分割次数。
    # https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/dong-tai-gui-hua-by-liweiwei1419-2/
    def minCut(self, s: str) -> int:
        if len(s)<2:return 0
        size = len(s)
        dp = [float('inf') for i in range(size)]
        for i in range(1, size):
            if s[:i+1] == s[:i+1][::-1]:                #0:i是回文串，不用分割
                dp[i] = 0
                continue
            tmpMin = float('inf')
            for j in range(i):                          #不是回文串，从头开始分割
                if s[j+1:i+1] == s[j+1:i+1][::-1]:      #后半段从j+1开始，j在上面已经包含过了
                    tmpMin = dp[j] + 1                  #分割后还是回文，那就是在上一次的基础上+1
                dp[i] = min(dp[i], tmpMin)              #取最少次数，就是在所有的分割中取最小的
            # dp[i] = min([dp[j] +1 for j in range(i) if s[j+1:i+1] == s[j+1:i+1][::-1] ])
        return dp[-1]


# @lc code=end
s = "aab"
o = Solution()
print(o.minCut(s))