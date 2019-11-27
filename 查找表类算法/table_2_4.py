#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/237/learn-to-use-dict/989/
# 根据字符出现频率排序
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
# 示例 1:
# 输入:
# "tree"
# 输出:
# "eert"
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

# 示例 2:
# 输入:
# "cccaaa"
# 输出:
# "cccaaa"
# 解释:
# 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
# 注意"cacaca"是不正确的，因为相同的字母必须放在一起。

# 示例 3:
# 输入:
# "Aabb"
# 输出:
# "bbAa"

# 解释:
# 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
# 注意'A'和'a'被认为是两种不同的字符。
import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 1: return s
        counter = collections.defaultdict(int)
        
        # 遍历时间复杂度为 O(N) 因为要建立一个字典存储元素, 此时空间复杂度最坏为O(N) N为字符长度
        for c in s:
            counter[c] = counter[c] + 1
        
        # 排序 平均最好的时间复杂度为O(Klog(K)) 最坏时间复杂度为O(K^2) K为字典键的数量
        sorted_array = sorted(counter.items(), key=lambda s:s[1], reverse=True)
        
        # 遍历排好序的数组 时间复杂度O(K) 空间复杂度O(N)
        string = ''
        for key, value in sorted_array:
            string += key * value   
        return string 

s = "tree"
ss = Solution()
re = ss.frequencySort(s)
print(re)

