# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.18.最短超串
# 
# https://leetcode-cn.com/problems/shortest-supersequence-lcci/
# 
# 假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。
# 返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。
# 
# 示例 1:
# 
# 输入:
# big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
# small = [1,5,9]
# 输出: [7,10]
# 
# 示例 2:
# 
# 输入:
# big = [1,2,3]
# small = [4]
# 输出: []
# 
# 提示：
# 
# 
# 	big.length <= 100000
# 	1 <= small.length <= 100000
# 
# 
# 
# Medium 41.9%
# Testcase Example: [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
# [1, 5, 9]
# 
# 提示:
# 从蛮力解法开始。
# 一种蛮力解决方案是对于每个起始位置不断向前移动，直到你找到一个包含所有目标字符的子序列为止。
# 另一种对蛮力方法的考虑是，我们取每个起始索引，在目标字符串中寻找每个元素的下一个出现位置。所有这些出现位置的最大值标志着子序列的尾部（该子序列包含所有目标字符）。这个算法的时间复杂度是多少？怎样才能使它更快呢？
# 考虑一下前面解释的蛮力解法。瓶颈在于我们反复查询某个特定字符的下一个出现位置。有办法优化该过程么？你应该能在O(1)时间内完成。
# 你能从每个索引中预先计算一个特定字符的出现位置吗？尝试使用一个多维数组。
# 在得到了预计算的解法之后，考虑一下如何降低空间复杂度。你应该能够将其降低到O(SB)的时间和O(B)的空间（其中B是较大数组的大小，S是较小数组的大小）。
# 另一种考虑方法是：假设你有一个每个元素所在索引的列表。你能找到包含所有元素的第一个子序列吗？你能找到第二个吗？
# 考虑使用堆。
# 
# 
from typing import List
class Solution:
    #滑动窗口
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        h = {}
        small = set(small)
        l, r = 0, 0
        minlen = float('inf')
        for i in range(len(big)):
            if big[i] in small:
                h[big[i]] = i                   #记录small中字符的最后出现位置
            if len(h) == len(small):            #全部匹配到了，找到最左和最右计算长度，记录最小值
                r_idx = max(h.values())         
                l_idx = min(h.values())
                if minlen > r_idx - l_idx:
                    l, r = l_idx, r_idx
                    minlen = r_idx - l_idx
        if len(h) != len(small):                #big全部找完，还是缺少small中的字符
            return []
        return [l,r]
    




big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
o = Solution()
print(o.shortestSeq(big, small))
