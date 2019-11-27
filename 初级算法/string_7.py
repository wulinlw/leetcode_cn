#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/38/
# 实现 strStr()
# 实现 strStr() 函数。

# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

# 示例 1:

# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:

# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:

# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
class Solution(object):
    # https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hl = len(haystack)
        nl = len(needle)
        if nl == 0:
            return 0
        if nl > hl:
            return -1
        idx = 0
        while True:
            # print idx,haystack[idx]
            if idx >= hl:
                return -1
            if (idx + nl) > hl:
                return -1
            if haystack[idx] == needle[0]:
                if self.diff(haystack, needle, idx):
                    return idx
            idx += 1

    def diff(self, haystack, needle, i):
        c = 0
        while True:
            if (c >= len(haystack)) or (c >= len(needle)):
                return False
            # print '--',i,c,haystack[i],needle[c]
            if haystack[i] != needle[c]:
                return False
            if c == len(needle) - 1:
                return True
            c += 1
            i += 1

    # 作弊
    def strStr_py(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not len(needle):
            return 0
        i = haystack.find(needle)
        return i

    # kmp算法
    # 理解看下面的
    # http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
    # https://leetcode-cn.com/problems/implement-strstr/solution/kmpshi-xian-by-jia-zhi-tong-1/
    def strStr4(self, haystack, needle):
        if needle == "":
            return 0
        
        # 生成next的算法
        # a  b a b c
        # 0  0 1 2 0    从开始到当前位置，前缀和后缀的最大长度
        # -1 0 0 1 2    第一位固定-1，其他位一次后移一位
        # 则i=0时，next[1] = 0
        # 看上面例子index[3]的字符是b,已知他前一位index[2]的字符a == index[0]，
        # 那下一步想要相等，只需index[2+1] == index[0+1]即可
        # 如果相等，i,k都前进一步
        # 如果不相等，则将next[k]的值给k

        # pnext每一位存的是把pnext[index]移动到当前位置
        # 如上面的c不相等时，pnext[2]移动到当前位置
        # a  b a b c
        # -1 0 0 1 2
        #      a b a b c
        i = 0
        k = -1 #对比位的指针，从-1位开始，如果相等则K+1
        m = len(needle)
        pnext = [-1] * m
        while i < m - 1:
            # print(i, k,needle[i] , needle[k])
            if k == -1 or needle[i] == needle[k]:
                i = i + 1
                k = k + 1
                pnext[i] = k
            else:
                k = pnext[k]#右移needle
            # print(pnext)
        
        p_long  = 0
        p_short = 0 
        n = len(haystack)
        while p_short < m and p_long < n:
            if p_short == -1 or needle[p_short] == haystack[p_long]:
                p_short += 1
                p_long  += 1
            else:
                p_short = pnext[p_short]
                # -1的情况，就是第一位不匹配，需要把needle向后移动，
                # 由于0是头，那-1就是在向右移动了一位
        #短的跑完，匹配上了，指针就不会动了，起点就是长的-短的
        if p_short == m:
            return p_long-p_short
        return -1
    
    #自己写的next计算方法，正解
    def next(self,needle):
        # generate pnext
        i = 0
        p = 0
        m = len(needle)
        pnext = [0] * m
        pnext[0] = -1
        while i < m - 1:
            if pnext[i] == -1 or needle[p] != needle[i]:
                i+=1
            else :
                pnext[i+1] = pnext[i]+1
                i+=1
                p+=1
        return pnext

haystack = "hello"
needle = "ell"
# needle = "abcdabd"
# haystack = "aaaaa"
# needle = "a"
# haystack = "aaaaabcdefg"
# needle = "g"
# haystack = "mississippi"
# needle = "issipi"
# haystack = "a"
# needle = "a"
obj = Solution()
n = obj.strStr4(haystack, needle)
print('return', n)

# import random
# random.sample('zyxwvutsrqponmlkjihgfedcba',5)
# for i in range(10):
#     n1 = obj.strStr(haystack, needle)
#     n2 = obj.strStr2(haystack, needle)
#     if n1 !=n2:
#         print(n1,n2)