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
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        total_max=-1e10
        total_index=[0,0,0,0]
        dp=[[0]*n for _ in range(m)]
        dp[0]=matrix[0]
        for i in range(1,m):
            for j in range(0,n):
                dp[i][j]=dp[i-1][j]+matrix[i][j]

        for i in range(m):
            for j in range(i,m):
                
                lis=[dp[j][k]-(dp[i-1][k] if i!=0 else 0) for k in range(n)]
                start,end,lis_max=self.getlis(lis)
                if lis_max>total_max:
                    total_index=[i,start,j,end]
                    total_max=lis_max
        return total_index

    def getlis(self,lis):
        n=len(lis)
        lis_max,cur_max=lis[0],lis[0]
        start,end,max_start=0,0,0
        for i in range(1,n):
            if cur_max<0:
                cur_max=lis[i]
                start=i
            else:
                cur_max=cur_max+lis[i]
            
            if cur_max>lis_max:
                lis_max=cur_max
                max_start=start
                end=i
        return max_start,end,lis_max

matrix = [
   [-1,0],
   [0,-1]
]
o = Solution()
print(o.getMaxMatrix(matrix))






