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

    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        if len(s) < 2: return len(s) # 边界条件
        res = 1
        
        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head: tail]:
                res = max(tail - head + 1, res)
            else:
                while s[tail] in s[head: tail]:
                    head += 1
        return res

# 作者：z1m
# 链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/tu-jie-hua-dong-chuang-kou-shuang-zhi-zhen-shi-xia/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。    

s = "arabcacfr"
obj = Solution()
print(obj.longestSubstringWithoutDuplication(s))
