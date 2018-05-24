#!/usr/bin/python
#coding:utf-8
import math
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = len(str)
        i=0
        m = ["0","1","2","3","4","5","6","7","8","9"]
        n = []
        while i<l:
            if str[i] not in m:
                ltmp = len(n)
                if ltmp == 0 and str[i]!=" ":
                    if str[i] in ["-","+"]:
                        n.append(str[i])
                        i+=1
                        continue
                    else:
                        return 0
                elif ltmp>=1:
                    break
                i+=1
                continue
            n.append(str[i])
            i+=1
        print(n)
        l2 = len(n)

        if n ==["-"] or l2==0:
            return 0

        # 这里可以直接用int(n[:])
        p=0
        r = 0
        for idx,i in enumerate(n):
            if i in ["-","+"]:
                continue
            r += int(i)*(10**(l2-idx-1))
        print(r)
        if n[0] =="-":
            r=0-r
        if r>2147483647:
            return 2147483647
        elif r< -2147483648:
            return -2147483648
        else:
            return r


s = "42"
# s = "   -42"
s = "4193 with words"
s = "words and 987"
s = "-91283472332"
s = "+-2"
obj = Solution()
n = obj.myAtoi(s)
print('return', n)