#!/usr/bin/python
#coding:utf-8

# 替换空格
# 请实现一个函数，将一个字符串中的空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

class Solution(object):
    def replaceSpaceByAppend(self, s):
        re = []
        for i in s: 
            if i ==' ':
                re.append("%")
                re.append("2")
                re.append("0")
            else:
                re.append(i)
        return "".join(re)

        
s = "we are happy."
obj = Solution()
re = obj.replaceSpaceByAppend(s)
print(re)
