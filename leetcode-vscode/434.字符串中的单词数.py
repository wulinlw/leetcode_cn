#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (33.91%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 39.5K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
# 
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
# 
# 示例:
# 
# 输入: "Hello, my name is John"
# 输出: 5
# 
# 
#

# @lc code=start
class Solution:
    #碰到结尾算一个
    #不能处理"love live! mu'sic forever"中的单引号
    def countSegments2(self, s: str) -> int:
        n = len(s)
        if n==0:return 0 
        cur = 0
        wordCnt = 0
        while cur+1<=n-1:
            if not s[cur].isalpha():
                cur+=1
                continue
            #和删除重复链表2 思路一样
            while cur+1<=n-1 and s[cur].isalpha() and s[cur+1].isalpha():
                cur += 1
            cur += 1
            wordCnt += 1
        return wordCnt

    #碰到单词开头 空格+字母 算一个
    def countSegments(self, s: str) -> int:
        segment_count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1
        return segment_count


        
# @lc code=end

s = "Hello, my name is John"
s = "love live! mu'sic forever"
o  = Solution()
print(o.countSegments(s))