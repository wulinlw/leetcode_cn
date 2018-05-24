#!/usr/bin/python
#coding:utf-8
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

    def isPalindrome(self, s):
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