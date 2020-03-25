#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#
# https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (49.50%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    23.8K
# Total Submissions: 40.7K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
# 
# 返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
# 
# 
# 
# 示例 1：
# 
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 
# 
# 示例 2：
# 
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 
# 
# 示例 3：
# 
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] 和 str2[i] 为大写英文字母
# 
# 
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:              #有字符不一样的，不可能除尽
            return ""
        def gcd(a, b):                          #辗转相处
            return a if b==0 else gcd(b, a%b)
        print(gcd(len(str1), len(str2)))
        return str1[:gcd(len(str1), len(str2))]
        
# @lc code=end

str1 = "ABCABC"
str2 = "ABC"
o = Solution()
print(o.gcdOfStrings(str1, str2))