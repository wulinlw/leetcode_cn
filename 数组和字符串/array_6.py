#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/202/conclusion/792/
# 杨辉三角 II
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 示例:
# 输入: 3
# 输出: [1,3,3,1]
# 进阶：
# 你可以优化你的算法到 O(k) 空间复杂度吗？

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if(rowIndex==0):
            return [1]
        dp=[1,1]#第二行的dp
        for i in range(3,rowIndex+2):
            cur=[0]*(i)#当前行dp初始化为0
            cur[0]=cur[-1]=1#首尾设为0
            for j in range(1,i-1):
                cur[j]=dp[j-1]+dp[j]
            dp=cur#更新dp
        return dp


rowIndex = 3
s = Solution()
n = s.getRow(rowIndex)
print(n)       