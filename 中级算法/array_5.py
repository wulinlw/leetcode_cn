#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/79/
# 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

# https://zhuanlan.zhihu.com/p/43844178
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 根据回文的特性，一个大回文按比例缩小后的字符串也必定是回文，比如ABCCBA，那BCCB肯定也是回文。所以我们可以根据动态规划的两个特点：
        # （1）把大问题拆解为小问题
        # （2）重复利用之前的计算结果
        # 这道题。如何划分小问题，我们可以先把所有长度最短为1的子字符串计算出来，根据起始位置从左向右，这些必定是回文。
        # 然后计算所有长度为2的子字符串，再根据起始位置从左向右。
        # 到长度为3的时候，我们就可以利用上次的计算结果：如果中心对称的短字符串不是回文，那长字符串也不是，如果短字符串是回文，那就要看长字符串两头是否一样。
        # 这样，一直到长度最大的子字符串，我们就把整个字符串集穷举完了。
        
        # 使用动态规划，用空间换时间，把问题拆分
        # 获取字符串s的长度
        str_length = len(s)
        # 记录最大字符串长度
        max_length = 0
        # 记录位置
        start = 0
        # 循环遍历字符串的每一个字符
        for i in range(str_length):
            # print(1,i,start,max_length,s[i-max_length: i+1] ,s[i-max_length: i+1][::-1],s[i-max_length: i+1] == s[i-max_length: i+1][::-1])
            # print(2,i,start,max_length,s[i-max_length-1: i+1] , s[i-max_length-1: i+1][::-1],s[i-max_length-1: i+1] == s[i-max_length-1: i+1][::-1])
            # 如果当前循环次数-当前最大长度大于等于1  并  字符串[当前循环次数-当前最大长度-1:当前循环次数+1]  == 取反后字符串
            if i - max_length >= 1 and s[i-max_length-1: i+1] == s[i-max_length-1: i+1][::-1] :
                print("2",i,max_length,s[i-max_length-1: i+1])
                # 记录当前开始位置
                start = i - max_length - 1
                # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
                max_length += 2
                continue
            # 如果当前循环次数-当前最大长度大于等于0  并  字符串[当前循环次数-当前最大长度:当前循环次数+1]  == 取反后字符串
            if i - max_length >= 0 and s[i-max_length: i+1] == s[i-max_length: i+1][::-1] :
                print("1",i,max_length,s[i-max_length: i+1])
                start = i - max_length
                # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
                max_length += 1
                
        # 返回最长回文子串
        return s[start: start + max_length]

    





nums = "bacbadabds"
s = Solution()
n = s.longestPalindrome(nums)
print(n)



