#!/usr/bin/python
#coding:utf-8

# // 面试题49：丑数
# // 题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到
# // 大的顺序的第1500个丑数。例如6、8都是丑数，但14不是，因为它包含因子7。
# // 习惯上我们把1当做第一个丑数。
import heapq
class Solution:
    # dp[i] 表示第i个丑数
    # 那么dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
    # 这里 l_2, l_3, l_5是表示，指到的位置。
    # 时间复杂度：O(n)
    def GetUglyNumber(self, n):
        if n == 0:return
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            if dp[i] >= 2 * dp[l_2]:
                l_2 += 1
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]
        # 作者：powcai
        # 链接：https://leetcode-cn.com/problems/ugly-number-ii/solution/dui-he-dong-tai-gui-hua-by-powcai/

    def GetUglyNumber2(self, index):
        if index == 0:return
        factors = [2,3,5]
        heap = factors + [1]
        heapq.heapify(heap)
        while index>1:
            small = heapq.heappop(heap)
            for factor in factors:
                new = small * factor
                if new not in heap:
                    heapq.heappush(heap, new)
            index -= 1
        return heapq.heappop(heap)
        
n = 1500
n=20
obj = Solution()
print(obj.GetUglyNumber(n))
print(obj.GetUglyNumber2(n))
