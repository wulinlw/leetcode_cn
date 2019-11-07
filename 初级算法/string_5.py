#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/36/
# 验证回文字符串
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:

# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:

# 输入: "race a car"
# 输出: false
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 0:
            return True
        s = s.lower()
        i = 0
        j = l - 1
        while (i < j):
            # print(i,j,s[i].isalnum(),s[j].isalnum())
            if s[i].isalnum() == False:
                i += 1
                continue
            if s[j].isalnum() == False:
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome2(self, s):
        import re
        pattern = re.compile('[\W]+')
        s = pattern.sub('', s).lower()
        return s == s[::-1]


# s = "A man, a plan, a canal: Panama"
s = "race a car"
# s = "0P"
obj = Solution()
n = obj.isPalindrome(s)
print('return', n)