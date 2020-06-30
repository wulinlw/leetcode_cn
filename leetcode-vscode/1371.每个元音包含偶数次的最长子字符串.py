# #!/usr/bin/python
# #coding:utf-8
# 
# 1371.每个元音包含偶数次的最长子字符串
# 
# https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
# 
# 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 &#39;a&#39;，&#39;e&#39;，&#39;i&#39;，&#39;o&#39;，&#39;u&#39; ，在子字符串中都恰好出现了偶数次。
#  
# 
# 示例 1：
# 
# 
# 输入：s = "eleetminicoworoep"
# 输出：13
# 解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "leetcodeisgreat"
# 输出：5
# 解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "bcbcbc"
# 输出：6
# 解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
# 
# 
#  
# 
# 提示：
# 
# 
# 	1 <= s.length <= 5 x 10^5
# 	s 只包含小写英文字母。
# 
# 
# 
# Medium 52.6%
# Testcase Example: "eleetminicoworoep"
# 
# 提示:
# Represent the counts (odd or even) of vowels with a bitmask.
# Precompute the prefix xor for the bitmask of vowels and then get the longest valid substring.
# 
# 

class Solution:
    # 前缀和+状态压缩 
    # 如果坐标 i 对应的状态码是 00011，坐标 j 对应的状态码是 00011，那么他们俩中间的元音字母数一定是偶数
    def findTheLongestSubstring(self, s: str) -> int:
        re, status, n = 0, 0, len(s)            
        pos = [-1] * (1 << 5)                   #二进制的低5位分别表示5个元音的奇偶，0偶 1奇，32位数组
        pos[0] = 0
        # print(pos)
        for i in range(n):
            if s[i] == 'a':                     #aeiou出现位置用二进制的1，2，3，4标记，0偶 1奇
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            # print(status)
            if pos[status] != -1:               #不等于-1说明之前出现过，用当前索引-上次出现的索引就是子串的长度，更新下最大值
                re = max(re, i+1-pos[status])
            else:
                pos[status] = i+1               #第一次出现，记录元音出现奇偶状态的初始索引
        # print(pos)
        return re
                    

s = "eleetminicoworoep"
# s = "bcbcbc"
o = Solution()
print(o.findTheLongestSubstring(s))
# print(1<<4)
