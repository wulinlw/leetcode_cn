#!/usr/bin/python
#coding:utf-8

# 表示数值的字符串
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

# 定义两个标志位，分别表示E或者e是否出现过，以及小数点.是否出现过。
# 1. 以e（或E）为分隔，获得两个子字符串；e之前的字符串小数点只能出现一次；e之后的字符串不允许出现小数点；
# 2. 符号位+或-只可能出现在两个子字符串的首位；
# 3. e（或E）、小数点.不能出现在末尾
class Solution:
    def isNumeric(self, s):
        if not s: return False
        hasE = False            #是否有E
        hasSign  = False        #是否有符号
        isDecimal = False       #是否小数
        for i in range(len(s)):
            if s[i] in ['e','E']:
                if hasE or i==len(s)-1: #2个e或，e在结尾  不合法
                    return False
                hasE = True
            elif s[i] == '.':
                if hasE or isDecimal:   #e后面不能有小数， 点不能重复
                    return False
                isDecimal = True
            elif s[i] in ['-','+']:
                if hasSign and s[i-1] not in ['e','E']:             #之前有符号，当前符号不再e前面，正常的是-1e-12
                    return False
                if not hasSign and i>0 and s[i-1] not in ['e','E']: #之前无符号，不是首位
                    return False
                hasSign = True
            elif s[i]<"0" or s[i]>"9":
                return False
        return True
    


obj = Solution()
#以下是true
print(obj.isNumeric('+100'))
print(obj.isNumeric('2e5'))
print(obj.isNumeric('e3'))
print(obj.isNumeric('-123'))
print(obj.isNumeric('3.1415'))
print(obj.isNumeric('-1e-16'))

#以下是false
print(obj.isNumeric('12e'))
print(obj.isNumeric('1a3.14'),1)
print(obj.isNumeric('1.2.3'))
print(obj.isNumeric('+-5'))
print(obj.isNumeric('12e+5.4'))