#!/usr/bin/python
#coding:utf-8

# 正则表达式匹配
# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
# 模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

# 而当模式中的第二个字符是*时：
# 如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
# 1. 模式后移2字符，相当于x*被忽略                                  aa      a*aa     *取0的情况  ,重点就是*取0，1，>1的3种情况
# 2. 字符串后移1字符，模式后移2字符                                 aaa     a*aa     *取1的情况
# 3. 字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位   aaaa    a*a      *取>1的情况

class Solution:
    def match(self, s, pattern):
        if len(s)==0 and len(pattern)==0:return True
        if len(s)!=0 and len(pattern)==0:return False
        if not pattern:return not s
        if len(pattern) > 1 and pattern[1] =='*':
            if not s: 
                return self.match(s[:], pattern[2:])
            if s[0] == pattern[0] or pattern[0] == '.':         #第一位匹配
                return self.match(s[1:], pattern[2:]) or \
                       self.match(s[1:], pattern[:]) or \
                       self.match(s[:], pattern[2:])
            else:                                               #第一位匹配不匹配时，模式后移2位, aa, b*aa 这里的b*就是后移的2位
                return self.match(s[:], pattern[2:])            #即*取0的情况
        if s and (s[0] == pattern[0] or pattern[0] == '.'):     #.都后移一位  ，这段放在后面是因为需要优先考虑第二位是*的情况
            return self.match(s[1:], pattern[1:])
        return False

    # 方法一：回溯
    # 首先，我们考虑只有 '.' 的情况。这种情况会很简单：我们只需要从左到右依次判断 s[i] 和 p[i] 是否匹配。
    # def isMatch(self,s:str, p:str) -> bool:
    #     if not p: return not s # 边界条件
    #     first_match = s and p[0] in {s[0],'.'} # 比较第一个字符是否匹配
    #     return first_match and self.isMatch(s[1:], p[1:])
    # 如果有星号，它会出现在 p[1] 的位置，这时有两种情况：
    # 星号代表匹配 0 个前面的元素。如 '##' 和 a*##，这时我们直接忽略 p 的 a*，比较 ## 和 ##；
    # 星号代表匹配一个或多个前面的元素。如 aaab 和 a*b，这时我们将忽略 s 的第一个元素，比较 aab 和 a*b。
    # 以上任一情况忽略掉元素进行比较时，剩下的如果匹配，我们认为 s 和 p 是匹配的。
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        # 第一个字母是否匹配
        first_match = bool(s and p[0] in {s[0],'.'})
        # 如果 p 第二个字母是 *
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or \
            first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    # 动态规划，思路和回溯一样
    def isMatch2(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j==len(p):
                return i==len(s)
            first = i<len(s) and p[j] in ['.', s[i]]
            if j<=len(p)-2 and p[j+1]=='*':
                answer=first and dp(i+1,j) or dp(i,j+2)
            else:
                answer = first and dp(i+1,j+1)
            memo[(i,j)] = answer
            return answer
        return dp(0,0)


s = 'aaa'
pattern = 'a.a'
obj = Solution()
print(obj.match(s, 'a.a'))
print(obj.match(s, 'ab*ac*a'))
print(obj.match(s, 'aa.a'))
print(obj.match(s, 'ab*a'))
print(obj.match('aa', 'a*'))
print(obj.isMatch('ab', 'c'))
print(obj.isMatch('', '.*c'))
print(obj.isMatch('ab', '.*c'))
print(obj.isMatch('', 'b*'))
print(obj.isMatch('a', 'ab*'))
print(obj.isMatch('aa', 'a*'))