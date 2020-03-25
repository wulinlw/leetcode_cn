#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
# https://leetcode-cn.com/problems/is-subsequence/description/
#
# algorithms
# Easy (48.05%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    29.4K
# Total Submissions: 60.8K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 
# 
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 
# 示例 1:
# s = "abc", t = "ahbgdc"
# 
# 返回 true.
# 
# 示例 2:
# s = "axc", t = "ahbgdc"
# 
# 返回 false.
# 
# 后续挑战 :
# 
# 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
# 
# 致谢:
# 
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
# 
#

# @lc code=start
class Solution:
    def isSubsequence2(self, s: str, t: str) -> bool:
        i,j = 0,0 
        while i<len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

    #labuladong的算法小抄 二分查找高效判定子序列
    def isSubsequence(self, s: str, t: str) -> bool:  
        from collections import defaultdict
        import bisect
        lookup = defaultdict(list)
        for idx, val in enumerate(t):       #记录每一个字符出现的所有坐标
            lookup[val].append(idx)
        # print(lookup)

        # 匹配时，在字符坐标列表lookup中找下一个比loc大的即可，不存在或比坐标列表长就是没有
        loc = -1                                        #第一个坐标要设为-1，避免只出现一次的字符情况下，出现问题
        for a in s:
            j = bisect.bisect_left(lookup[a], loc + 1)  #在a的坐标列表中找比loc大的那个，如果这个值在最后，就是坐标中没有
            if j >= len(lookup[a]): return False
            loc = lookup[a][j]                          #更新最新的坐标
        return True 
        
# @lc code=end

s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
# s = "axc"
# t = "ahabgdc"
o = Solution()
print(o.isSubsequence(s, t))