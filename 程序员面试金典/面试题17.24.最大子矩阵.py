#!/usr/bin/python
#coding:utf-8

# 面试题 17.24. 最大子矩阵
# 给定一个正整数和负整数组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
# 返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。
# 注意：本题相对书上原题稍作改动
# 示例:
# 输入:
# [
#    [-1,0],
#    [0,-1]
# ]
# 输出: [0,1,0,1]
# 解释: 输入中标粗的元素即为输出所表示的矩阵
# 说明：

# 1 <= matrix.length, matrix[0].length <= 200
# https://leetcode-cn.com/problems/max-submatrix-lcci/


from typing import List
class Solution:
    # https://leetcode-cn.com/problems/max-submatrix-lcci/solution/pythondong-gui-ji-bai-shuang-100-by-qiu-feng-si-lu/
    def getMaxMatrix2(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        maxArea = -1e10
        total_index = [0,0,0,0]
        dp = [[0]*n for _ in range(m)]
        dp[0] = matrix[0]
        for i in range(1,m):
            for j in range(0,n):
                dp[i][j] = dp[i-1][j] + matrix[i][j]

        for i in range(m):
            for j in range(i,m):
                
                lis = [dp[j][k]-(dp[i-1][k] if i!=0 else 0) for k in range(n)]
                # print(i,j,lis)
                start,end,lis_max = self.getlis1(lis)
                if lis_max > maxArea:
                    total_index = [i,start,j,end]
                    maxArea = lis_max
        return total_index

    def getlis1(self,lis):
        n = len(lis)
        lis_max,curSum = lis[0],lis[0]
        start,end,start = 0,0,0
        for i in range(1,n):
            if curSum<0:
                curSum=lis[i]
                start=i
            else:
                curSum=curSum+lis[i]
            
            if curSum>lis_max:
                lis_max=curSum
                start=start
                end=i
        return start,end,lis_max
    
    #leetcode 363 代码套路一样
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        maxArea = float('-inf')                     #最大面积
        res = [0, 0, 0, 0]

        for left in range(col):                     #从左到右，从上到下，滚动遍历
            colSum = [0] * row                      #以left为左边界，每行的总和
            for right in range(left, col):          #这一列每一位为右边界
                for i in range(row):                #遍历列中每一位，计算前缀和
                    colSum[i] += matrix[i][right]

                startX, endX, maxAreaCur= self.getMax(colSum)#在left，right为边界下的矩阵中，前缀和colSum的最大值
                if maxAreaCur > maxArea:
                    res = [startX, left, endX, right]      #left是起点y轴坐标，right是终点y轴坐标
                    maxArea = maxAreaCur
        return res
    
    #这一列中，找最大值，同时记录起点，终点
    #因为传进来的是列的前缀和，所以返回的起点、终点代表行坐标
    def getMax(self, nums):
        n = len(nums)
        maxVal, curSum = nums[0], nums[0]       #初始化最大值
        startIndex, end, start = 0, 0, 0        #初始化临时起点，起点，终点
        for i in range(1,n):
            if curSum<0:                        #前缀和小于0了，前面就不要了，从当前开始
                curSum = nums[i]
                startIndex = i                  #前面的前缀和小于0了，需要重置起点，从当前开始才有可能成为最大值
            else:
                curSum = curSum + nums[i]
            
            if curSum > maxVal:
                maxVal = curSum
                start = startIndex             #记录下前面的起点，默认0，或者是curSum<0后，重新更新的起点
                end = i                        #终点是当前坐标
        return start, end, maxVal              #起点，终点，最大前缀和（最大面积）

matrix = [
   [-1,0],
   [0,-1]
]
matrix = [
   [-1,0,0,0,0],
   [0,-1,1,2,3],
   [0,-1,0,0,0]
]
o = Solution()
print(o.getMaxMatrix(matrix))






