#!/usr/bin/python
#coding:utf-8

# // 面试题48：最长不含重复字符的子字符串
# // 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子
# // 字符串的长度。假设字符串中只包含从'a'到'z'的字符。

class Solution:
    def longestSubstringWithoutDuplication(self, s):
        if len(s) == 0:return
        maxLen = 0
        curLen = 0
        dp = [-1] * 26
        for i in range(len(s)):
            p = ord(s[i])-ord('a')              #97-[a-z]保证在26以内，匹配dp
            if dp[p] == -1 or i-dp[p]>maxLen:   #未出现或 当前出现到上次出现的距离>最大长度
                curLen += 1
            else:                               #当前出现到上次出现的距离<=最大长度
                curLen = i-dp[p]                #更新为 当前出现到上次出现的距离
            if curLen>maxLen:
                maxLen = curLen
            dp[p] = i
        return maxLen

    # 滑动窗口,看这个
    # https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/tu-jie-hua-dong-chuang-kou-shuang-zhi-zhen-shi-xia/
    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        m = {}      #存在的字符坐标
        l = 0
        re = 0
        for r in range(n):
            if s[r] in m:           #重复了，移动左边界到重复值的下一位
                l = max(l, m[s[r]])
            m[s[r]] = r+1
            re = max(re, r-l+1)
        return re 

    # O(n2)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        Set = set()
        left,right,longest = 0, 0 ,0 
        while right < len(s):
            while s[right] in Set:
                Set.remove(s[left])
                left += 1 
            Set.add(s[right])
            right += 1 
            longest = max(right-left,longest)
        return longest


s = "arabcacfr"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
