#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/913/
# 螺旋矩阵 II
# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

# 示例:
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # https://leetcode-cn.com/problems/spiral-matrix-ii/solution/gu-ding-tao-lu-peng-dao-bian-jie-jiu-zhuan-xiang-p/
        res=[[False]*n for _ in range(n)]# 生成n*n的矩阵,用于标记是否已生成
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        # 实际表示的是这个方向上x,y每一步的步进长度
        # 如向右时，x不变，Y+1
        x,y=0,0#当前坐标
        count=0
        
        for i in range(1,n*n+1):
            res[x][y]=i
            dir_x,dir_y=directions[count][0],directions[count][1]
            # print(dir_x,dir_y)
            if(0<=x+dir_x<n and 0<=y+dir_y<n and not res[x+dir_x][y+dir_y]):#未到边界，且当前值未复制
                x=x+dir_x
                y=y+dir_y
            else:
                count=(count+1)%4#边界转向
                x=x+directions[count][0]
                y=y+directions[count][1]
            # print('--->',x,y)
        return res

        







n = 3
target = 1
s = Solution()
n = s.generateMatrix(n)
print(n)       