#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#
# https://leetcode-cn.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (50.45%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 16.2K
# Testcase Example:  '"00110"'
#
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
# 
# 重复出现的子串要计算它们出现的次数。
# 
# 示例 1 :
# 
# 
# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
# 
# 请注意，一些重复出现的子串要计算它们出现的次数。
# 
# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
# 
# 
# 示例 2 :
# 
# 
# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
# 
# 
# 注意：
# 
# 
# s.length 在1到50,000之间。
# s 只包含“0”或“1”字符。
# 
# 
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        cur = 0     #当前字符的个数，111 就是3个
        pre = 0     #前一种字符的个数
        cnt = 0     #结果
        for i in range(n):
            if s[i]==s[i-1]:
                cur+=1          #相同字符串，cur+1
            else:
                pre = cur       #碰到不同的，记录下前一个字符的个数，当前的字符从1开始计数cur
                cur = 1
            if pre>=cur:        #前一个字符长度>=现在的就是存在组合 111000有111000 1100 10
                cnt += 1
        return cnt
# @lc code=end

o  = Solution()
print(o.countBinarySubstrings("00110011"))
print(o.countBinarySubstrings("10101"))
