#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (35.55%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    32.1K
# Total Submissions: 90.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
import collections
class Solution:
    #滑动窗口
    def minWindow(self, s: str, t: str) -> str:
        start = 0 
        minlen = float('inf')
        left, right = 0, 0
        window = collections.defaultdict(int)   #窗口
        need = collections.defaultdict(int)     #t中字符数
        match = 0                               #窗口中已匹配字符数
        for i in t:                             #计算t中字符数
            need[i] += 1                
        # print(need)

        while right < len(s):
            ch = s[right]                       
            if ch in need:                      #是t中的字符，在window中+1
                window[ch] += 1
                if window[ch] == need[ch]:      #此字符数window==need时，总匹配数+1
                    match += 1
            right += 1                          #向右滑动一位

            while match == len(need):           #匹配了t的所有字符，right不动了，left向右走，缩小窗口，直到出现不能全部匹配
                if right-left < minlen:         #打破记录，更新起点，minlen
                    start = left 
                    minlen = right - left
                ch2 = s[left]
                if ch2 in need:                 #是t中的字符，在window中-1
                    window[ch2] -= 1
                    if window[ch2] < need[ch2]: #划出这个字符后，比need中的此字符少了，总匹配数-1
                        match -= 1
                left += 1                       #继续左滑
        #     print(window)
        # print(start,minlen)
        return "" if minlen==float('inf') else s[start : start+minlen]

# @lc code=end

S = "ADOBECODEBANC"
T = "ABC"
o = Solution()
print(o.minWindow(S, T))