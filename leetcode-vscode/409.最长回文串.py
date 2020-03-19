#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (52.07%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    22.1K
# Total Submissions: 41.6K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#
import collections
# @lc code=start
class Solution:
    # 偶数个c，总是可以放到中心的两侧c/2 | c/2
    # 回文串最多只有中点是一个
    def longestPalindrome2(self, s: str) -> int:
        re = 0
        count = collections.Counter(s)
        for i in count.values(): 
            re += i//2 *2               #取偶数个，放在中点两边
            if i%2==1 and re%2==0:      #总数是偶数的时候，中点可以放一个奇数的字符，当总数是奇数时后面都不用奇数了
                re += 1
        return re

    def longestPalindrome(self, s: str) -> int:
        re = 0
        count = collections.Counter(s)
        for i in count.values(): 
            re += i%2                   #统计奇数有多少
        return len(s) if re==0 else len(s)-re+1     
        #都是偶数，那全部都可以组成会问串，
        #只要有奇数，那总数-奇数就是所有偶数放入回文串中+1个奇数放到中点

# @lc code=end

s = "abccccdd"
o = Solution()
print(o.longestPalindrome(s))