#!/usr/bin/python
#coding:utf-8
class Solution(object):
    ans = ["1"]

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        while len(self.ans) < n:
            self.ans.append(self.getNext(int(self.ans[-1])))
        return self.ans[n - 1]

    def getNext(self, s):
        s = list(str(s))
        temp, cnt, res = -1, 1, ""
        for num in s:
            if num == str(temp):
                cnt += 1
            else:
                if temp != -1:
                    res += (str(cnt) + str(temp))
                temp, cnt = num, 1
        res += (str(cnt) + str(temp))
        return res


n = 1
n = 2
obj = Solution()
r = obj.countAndSay(n)
print('return', r)
