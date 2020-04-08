 #
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (60.80%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    22.2K
# Total Submissions: 36.3K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 
# 示例 1:
# 
# 
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
# 
# 
# 示例 2:
# 
# 
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 注意:
# 
# 
# 输入的字符串长度不会超过1000。
# 
# 
#

# @lc code=start
class Solution:
    #动态规划
    # dp[i][j] 表示字符串在i..j之间的子串是否是回文串
    # s[i] == s[j]      字符相等时true
    # j-i<2 or          只有1-2字符，是不是回文
    # dp[i+1][j-1]      回文向两边各扩展一个字符，是不是回文
    # 状态转移方程：dp[i][j] = dp[i+1][j-1] && str[i]==str[j]
    def countSubstrings(self, s: str) -> int:
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        re = 0
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i-j<2 or dp[i-1][j+1]):    #2边相等时，只有1-2个字符， or 3个及以上，那就看王两边扩展了还是不是回文
                    dp[i][j] = True
                    re += 1
            # print(dp[i])
        return re

    # 从中心往两侧延伸
    # 在长度为 N 的字符串中，可能的回文串中心位置有 2N-1 个：字母，或两个字母中间。
    # left和right指针和中心点的关系是？
    # 首先是left，有一个很明显的2倍关系的存在，其次是right，可能和left指向同一个（偶数时），也可能往后移动一个（奇数）
    # 大致的关系出来了，可以选择带两个特殊例子进去看看是否满足。
    def countSubstrings2(self, S):
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = center / 2                                   #中心2n，所以每一个点的中间再除以2
            right = left + center % 2                           #奇数时后移一位
            while left >= 0 and right < N and S[left] == S[right]:  #相等就往2边扩展
                ans += 1
                left -= 1
                right += 1
        return ans

    #从中心往两侧延伸，更好理解
    def countSubstrings3(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                self.res += 1
                i -= 1
                j += 1

        for i in range(n):
            helper(i, i)        #假设回文是奇数，中心只有一个
            helper(i, i + 1)    #假设回文是偶数，中心是中间2个
        return self.res

        
# @lc code=end
s = "abc"
# s = "aaa"
# s = "fdsklf"
o = Solution()
print(o.countSubstrings(s))