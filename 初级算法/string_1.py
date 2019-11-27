#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/32/
# 反转字符串
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 

# 示例 1：

# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 示例 2：

# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        arr.reverse()
        return ''.join(arr)

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s[::-1]
        return arr

    def reverseString(self, s):
        arr = list(s)
        s = 0
        r = len(arr)-1
        while s<r:
            arr[s],arr[r] = arr[r],arr[s]
            s+=1
            r-=1
        return ''.join(arr)
        
s = "hello"
ss = Solution()
n = ss.reverseString(s)
print('return', n)
