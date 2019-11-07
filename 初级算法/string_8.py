#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/39/
# 报数
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

# 注意：整数顺序将表示为一个字符串。

 

# 示例 1:

# 输入: 1
# 输出: "1"
# 示例 2:

# 输入: 4
# 输出: "1211"
class Solution(object):
    ans = ["1"]

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        while len(self.ans) < n:
            self.ans.append(self.getNext(int(self.ans[-1])))
        print(self.ans)
        return self.ans[n - 1]

    def getNext(self, s):
        s = list(str(s))
        temp, cnt, res = -1, 1, ""
        for num in s:
            if num == str(temp):#与前一个相同，数字加1
                cnt += 1
            else:
                if temp != -1:#第一个数字不是1，说1个当前数（如，2开头是说1个2，则12）
                    res += (str(cnt) + str(temp))
                temp, cnt = num, 1#几个（cnt）+ temp 
        res += (str(cnt) + str(temp))
        return res


n = 1
n = 4
obj = Solution()
r = obj.countAndSay(n)
print('return', r)
