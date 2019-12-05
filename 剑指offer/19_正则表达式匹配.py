#!/usr/bin/python
#coding:utf-8

# 正则表达式匹配
# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
# 模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

# 而当模式中的第二个字符是*时：
# 如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
# 1. 模式后移2字符，相当于x*被忽略；
# 2. 字符串后移1字符，模式后移2字符；
# 3. 字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位；

class Solution:
    def match(self, s, pattern):
        if len(s)==0 and len(pattern)==0:return True
        if len(s)!=0 and len(pattern)==0:return False
        if len(pattern) > 1 and pattern[1] =='*':
            if s[0] == pattern[0] or pattern[0] == '.':
                return self.match(s[1:], pattern[2:]) or \
                       self.match(s[1:], pattern[:]) or \
                       self.match(s[:], pattern[2:])
            else:
                return self.match(s[:], pattern[2:])
        if s and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False


s = 'aaa'
pattern = 'a.a'
obj = Solution()
print(obj.match(s, 'a.a'))
print(obj.match(s, 'ab*ac*a'))
print(obj.match(s, 'aa.a'))
print(obj.match(s, 'ab*a'))