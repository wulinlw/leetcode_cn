#!/usr/bin/python
#coding:utf-8

# 面试题 01.03. URL化
# URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。
# （注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）

# 示例1:

#  输入："Mr John Smith    ", 13
#  输出："Mr%20John%20Smith"
# 示例2:

#  输入："               ", 5
#  输出："%20%20%20%20%20"
# 提示：

# 字符串长度在[0, 500000]范围内。
# https://leetcode-cn.com/problems/string-to-url-lcci/

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        s = list(S[:length])
        cnt = s.count(" ")
        re = [0]*(len(s)+2*cnt)
        i = len(s)-1
        j = len(re)-1
        while i>=0:
            if s[i]!=' ':
                re[j] = s[i]
                j-=1
            else: 
                re[j] = "0"
                re[j-1] ="2"
                re[j-2] = "%"
                j-=3
            i-=1 
            # print(re)
        # print(len(re),re)
        return "".join(re)

s = "Mr John Smith    "
o  = Solution()
print(o.replaceSpaces(s, 13))
print(o.replaceSpaces("       ", 5))