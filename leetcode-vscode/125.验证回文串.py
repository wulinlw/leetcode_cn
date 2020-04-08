#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (42.49%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    93.3K
# Total Submissions: 216K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            while l<r and  not s[l].isalnum():      #过滤数字和字符
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1 
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# @lc code=end
s = "A man, a plan, a canal: Panama"
s = "0P"
o = Solution()
print(o.isPalindrome(s))