#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (35.53%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 47.7K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 示例 1:
# 
# 
# 输入: "aba"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
# 
# 注意:
# 
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
# 
# 
#

# @lc code=start
class Solution:
    #双指针
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1  
        while l<r:
            if s[l] != s[r]:                            #不相等时，
                a = s[l+1:r+1]                          #舍弃左字符，r+1包含r
                b = s[l:r]                              #舍弃右字符，不包含r
                return a == a[::-1] or b == b[::-1]
            l += 1                                      #相等时往中间走
            r -= 1
        return True

    #超时
    def validPalindrome2(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
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

        for i in range(len(s)):
            if isPalindrome(s[:i]+s[i+1:]):
                return True
        return False
# @lc code=end
s = "aba"
o = Solution()
print(o.validPalindrome(s))