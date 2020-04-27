# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题08.10.颜色填充
# 
# https://leetcode-cn.com/problems/color-fill-lcci/
# 
# 颜色填充。编写函数，实现许多图片编辑软件都支持的“颜色填充”功能。给定一个屏幕（以二维数组表示，元素为颜色值）、一个点和一个新的颜色值，将新颜色值填入这个点的周围区域，直到原来的颜色值全都改变。
#  示例1:
# 
# 
#  输入：
# image = [[1,1,1],[1,1,0],[1,0,1]] 
# sr = 1, sc = 1, newColor = 2
#  输出：[[2,2,2],[2,2,0],[2,0,1]]
#  解释: 
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。
# 
# 
#  说明：
# 
# 
# image 和 image[0] 的长度在范围 [1, 50] 内。
# 给出的初始点将满足 0 &lt;= sr &lt; image.length 和 0 &lt;= sc &lt; image[0].length。
# image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
# 
# 
# 
# Easy 54.2%
# Testcase Example: [[1,1,1],[1,1,0],[1,0,1]]
# 1
# 1
# 2
# 
# 提示:
# 把这个看成一个图。
# 你可以使用深度优先搜索（或广度优先搜索）。“正确”颜色的每个相邻像素都是一个连接边。
# 
# 
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(r, c):
            image[r][c] = newColor
            for i in [(0,1), (0,-1), (1,0), (-1,0)]:
                newr,newc = r+i[0], c+i[1]
                if 0<=newr<len(image) and 0<=newc<len(image[0]):
                    if image[newr][newc] == originColor:
                        dfs(newr,newc)

        originColor = image[sr][sc]
        if originColor == newColor:return image
        dfs(sr, sc)
        return image

image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]] 
sr = 1
sc = 1
newColor = 2
image = [
    [0,0,0],
    [0,1,1]] 
sr = 1
sc = 1
newColor = 1
o = Solution()
print(o.floodFill(image, sr,sc,newColor))