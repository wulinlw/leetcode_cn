#!/usr/bin/python
#coding:utf-8

# // 面试题58（二）：左旋转字符串
# // 题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# // 请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和数
# // 字2，该函数将返回左旋转2位得到的结果"cdefgab"。

class Solution:
    # 3次翻转
    # 1.翻转所有
    # 2.翻转第一段
    # 3.翻转第二段
    def LeftRotateString(self, s, n):
        if len(s) == 0 or n<1:return False
        s_len = len(s)
        s2 = list(s)
        s2 = s2[::-1]
        s2[:s_len-n] = s2[:s_len-n][::-1]
        s2[s_len-n:] = s2[s_len-n:][::-1]
        return "".join(s2)


s = "abcdefg"
n = 2
obj = Solution()
print(obj.LeftRotateString(s, 2))
