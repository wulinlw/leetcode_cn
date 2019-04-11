#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/114/
# Excel表列序号
# 给定一个Excel表格中的列名称，返回其相应的列序号。

# 例如，
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# 示例 1:

# 输入: "A"
# 输出: 1
# 示例 2:

# 输入: "AB"
# 输出: 28
# 示例 3:

# 输入: "ZY"
# 输出: 701
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。


class Solution(object):
    def titleToNumber(self, s):
        """
        :type n: int
        :rtype: int
        """
        result = 0 
        for letter in s:
            result = result * 26 + ord(letter) - ord('A') + 1#转换之后把大写字母对应的数字转化为小写字母。
        return result

    # 二十六进制转换为十进制，初始值是1
    def titleToNumber2(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s)-1,-1,-1):
            num += (ord(s[i]) - 64) * 26**(len(s)-i-1)
        return num


string = "AB"
s = Solution()
n = s.titleToNumber2(string)
print(n)









