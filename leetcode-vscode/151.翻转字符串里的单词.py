#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (36.04%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    43.9K
# Total Submissions: 113.3K
# Testcase Example:  '"the sky is blue"'
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 
# 
# 
# 示例 1：
# 
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 
# 
# 示例 2：
# 
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 
# 
# 示例 3：
# 
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 说明：
# 
# 
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 进阶：
# 
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
# 
#

# @lc code=start
class Solution:
    def reverseWords3(self, s: str) -> str:
        s = s.strip(' ')
        if len(s)<=1:return s
        n = len(s)-1
        i = j = n
        re = ""
        for i in range(n, -1, -1):
            if s[i] == ' ':
                while j>=0 and s[j]==' ' :
                    j -= 1
                if j>i:
                    re = re + " "+s[i+1:j+1]
                j = i
        if j>i:
            if j==n:
                re = re + " "+s[i:j+1] 
            else:
                re = re + " "+s[i:j]
        return re[1:]
    
    def reverseWords(self, s: str) -> str:
        re = " ".join(reversed(s.split()))
        return re

    # 看这个
    def reverseWords2(self, s: str) -> str:
        s = s.strip(' ')                               # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1    # 搜索首个空格
            res.append(s[i + 1: j + 1])             # 添加单词
            while s[i] == ' ': i -= 1               # 跳过单词间空格
            j = i                                   # j 指向下个单词的尾字符
        return ' '.join(res)
    
    def test(self):
        s = "the sky is blue"
        r1_1 = self.reverseWords(s)
        r1_2 = self.reverseWords2(s)
        r1_isEqual = (r1_1 == r1_2)

        s2 = "  hello world!  "
        r2_1 = self.reverseWords(s2)
        r2_2 = self.reverseWords2(s2)
        r2_3 = self.reverseWords3(s2)
        r2_isEqual = (r2_1 == r2_2)

        s3 = "a good   example"
        r3_1 = self.reverseWords(s3)
        r3_2 = self.reverseWords2(s3)
        r3_3 = self.reverseWords3(s3)
        r3_isEqual = (r3_1 == r3_2)
        print(r1_isEqual, r2_isEqual, r3_isEqual)

# @lc code=end
# s = "the sky is blue"
s = "  hello world!  "
s = "a good   example"
# s = "ab"
# s = " "
o = Solution()
# print(o.reverseWords3(s))
o.test()

# s = "the sky is blue"
# print(o.reverseWords(s)==o.reverseWords2(s))

# s = "  hello world!  "
# print(o.reverseWords(s)==o.reverseWords1(s))
# print(1,o.reverseWords(s),1)
# print(1,o.reverseWords1(s),1)

# s = "a good   example"
# print(o.reverseWords(s)==o.reverseWords1(s))
# print(1,o.reverseWords(s),1)
# print(1,o.reverseWords1(s),1)

# "the sky is blue"
# "  hello world!  "
# "a good   example"
# example   good a