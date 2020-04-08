#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
# https://leetcode-cn.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (31.42%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 22.6K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
# 
# 示例 1:
# 
# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 
# 
# 示例 2:
# 
# 输入: "abcd"
# 输出: "dcbabcd"
# 
#

# @lc code=start
class Solution:
    # kmp next数组算法
    # abbacd
    # 原s: abbacd, 长度记为 n
    # 逆r: dcabba, 长度记为 n
    # 如果我们把 abbacd dcabba看成一个字符串，中间加上一个分隔符 #，abbacd#dcabba
    # 判断abbacd#dcabba是否是回文，和kmp算法中计算next是一样的
    # 而我们中间加了分隔符，也就保证了前缀和后缀相等时，前缀一定在 abbacd 中
    # 而 next 数组是寻求最长的前缀，我们也就找到了开头开始的最长回文串。
    def shortestPalindrome(self, s: str) -> str:
        nextStr = s + '#' + s[::-1]
        b = [0] * (len(nextStr) + 1)
        j, i = -1, 0
        b[i] = j
        while i < len(nextStr): 
            while j>=0 and nextStr[i] != nextStr[j]:
                j = b[j]
            i += 1
            j += 1
            b[i] = j
        # print(b)
        return s[b[-1]:][::-1] + s              #计算的b[-1]就是最长的会文串，那s剩下的倒序放到开头即可

    # 双指针与递归
    # https://leetcode-cn.com/problems/shortest-palindrome/solution/zui-duan-hui-wen-chuan-by-leetcode/
    def shortestPalindrome2(self, s: str) -> str:
        n = len(s)
        i = 0
        for j in range(n-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        # print(i)
        if i == n: 
            return s
        remain_rev = s[i:n+1][::-1]
        return remain_rev + self.shortestPalindrome(s[:i]) + s[i:]
        # 返回从 i 到结尾的子字符串的反转 + 对从开头到 i−1 的子字符串进行shortestPalindrome过程 + 从 i 到结尾的子字符串







# @lc code=end
s = "aacecaaa"
s = "abcd"
o = Solution()
print(o.shortestPalindrome(s))