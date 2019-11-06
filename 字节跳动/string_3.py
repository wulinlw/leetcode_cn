#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1016/
# 字符串的排列
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。

# 示例1:
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
 
# 示例2:
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
 
# 注意：
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Sum = self.stringSum(s1)
        i = 0
        while i <= (len(s2)-len(s1)):
            # print(s2[i:len(s1)+i], self.stringSum(s2[i:len(s1)+i]))
            if s1Sum == self.stringSum(s2[i:len(s1)+i]):
                if self.confrim(s1, s2[i:len(s1)+i]):
                    return True
            i += 1
        return False

    def stringSum(self, string):
        sum = 0
        for i in string:
            sum += ord(i)
        return sum

    def confrim(self, s1, sub):
        i = 0
        while i <= len(sub)-1:
            if s1.count(s1[i]) != sub.count(s1[i]):
                return False
            i += 1
        return True

    # https://www.cnblogs.com/lightwindy/p/9764400.html
    def checkInclusion2(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        
        target = [0] * 26
        for x in A:
            target[x] += 1
        
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False

    # https://blog.csdn.net/qq_34771726/article/details/88650241
    def checkInclusion3(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        if l2<l1:         #若字符串s2的长度小于s1，则返回false
            return False
        
        s = 'abcdefghijklmnopqrstuvwxyz'
        dict1 = {}
        dict2 = {}
        for char in s:
            dict1[char] = 0          #初始化字典，key为字母，value为字母出现的次数，都初始化为0
            dict2[char] = 0
        for i in range(l1):
            dict1[s1[i]] += 1        # 首先计算前l1长度的不同字母出现次数
            dict2[s2[i]] += 1
        if dict1 == dict2:           # 若两个字典相等，则说明字符串的[0:l1]是字符串l1的不同排列
            return True
        for i in range(l2-l1):       # 开始往后查找，每次移动一个位置
            dict2[s2[i]] -= 1        # 减去滑动比较得前一个字母出现的次数
            dict2[s2[i+l1]] += 1     # 加上滑动后加进来的字母出现的次数
            if dict1 == dict2:       # 若相等，则返回true
                return True
        return False

s1 = "ab"
s2 = "eidbaooo"
s1= "ab"
s2 = "eidboaoo"
s1 = "abc"
s2 = "ccccbbbbaaaa"
s = Solution()
n = s.checkInclusion(s1, s2)
print(n)