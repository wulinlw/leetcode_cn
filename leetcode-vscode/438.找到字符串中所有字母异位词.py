#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (41.20%)
# Likes:    247
# Dislikes: 0
# Total Accepted:    21.8K
# Total Submissions: 51.4K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 
# 说明：
# 
# 
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 
# 
# 示例 1:
# 
# 
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0                                  #滑动窗口左边边界
        window = {}                                         #滑动窗口
        need = {}                                           #统计p的字符数
        re = []
        for i in p:
            need[i] = need.get(i,0) + 1
            
        for right in range(len(s)):                         #右边窗口滑动
            window[s[right]] = window.get(s[right], 0) + 1  #每次滑动新加入右侧值到window中
            if left + len(p) == right:                      #窗口满了，那就把左边的弹出去  
                if window[s[left]] == 1:                    #只有1个时需要删掉key，不然后面dict对比有问题
                    window.pop(s[left])
                else:
                    window[s[left]] -= 1
                left += 1                                   #左窗口右移一位
            if window == need:                              #一样就把左窗口坐标加入结果
                re.append(left)
        return re

# @lc code=end

s = "cbaebabacd"
p = "abc"

# s = "abab"
# p = "ab"

# s = "baa"
# p = "aa"
o = Solution()
print(o.findAnagrams(s, p))