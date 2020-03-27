#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.56%)
# Likes:    395
# Dislikes: 0
# Total Accepted:    146.4K
# Total Submissions: 369.5K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#

# @lc code=start
class Solution:
    # 最坏时间复杂度为 O((N−L)L)，最优时间复杂度为 O(N)
    def strStr2(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        if l2==0:return 0
        p1,p2 = 0,0
        while p1 < l1-l2+1: 
            while p1 < l1-l2-1 and haystack[p1] != needle[p2]:
                p1 += 1
            curlen = 0
            while p2<l2 and p1<l1 and haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
                curlen += 1
            if curlen==l2:
                return p1-l2
            p1 = p1-curlen+1
            p2 = 0
        return -1

    #kmp
    # https://leetcode-cn.com/problems/implement-strstr/solution/kmphua-48xiao-shi-kan-dong-liao-kmpxiang-rang-ni-z/
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        if l2==0:return 0
        if l1==0:return -1

        #构造next数组
        j, i = -1, 0                                #i在前，j在后面
        b = [0] * (l2 + 1)
        b[i] = j                                    #第一位-1
        while i<l2:
            while j>=0 and needle[i] != needle[j]:  #i,j不同时，更新j的值，再循环，一直向前回滚
                j = b[j]                            #回到前面一次出现的位置，一直可以回滚到b[j=0] = -1
            i += 1                                  #指向下一个字符
            j += 1                                  #匹配上了，后缀长度+1，推向下一位还相等就可以继续加，这样就计算出了相同前后缀的长度
            b[i] = j                                #后缀长度，更新到next数组
        # print(b)

        #开始匹配
        i, j = 0, 0                                 #j这回是text的， i是pattern的
        while j<l1: 
            while i>=0 and needle[i] != haystack[j]:#不同时，pattern指针根据next往回指
                i = b[i]
            i += 1 
            j += 1                                  #相同时向后推进
            if i == l2:                             #pattern匹配完成
                return j - l2
        return -1

# @lc code=end

haystack = "hello"
needle = "ll"
# haystack = "aaaaa"
# needle = "bba"
# haystack = "a"
# needle = "a"
haystack = "abacababaa"
needle = "ababaa"
o = Solution()
print(o.strStr(haystack, needle))