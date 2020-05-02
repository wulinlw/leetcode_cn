# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.19.水域大小
# 
# https://leetcode-cn.com/problems/pond-sizes-lcci/
# 
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
# 示例：
# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]
# 
# 提示：
# 
# 0 
# 0 
# 
# 
# 
# Medium 59.7%
# Testcase Example: [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
# 
# 提示:
# 如果给你一个指代水的单元格的行和列，你如何找到所有相邻的水域？
# 尝试递归计算含水单元格的数目。
# 你如何确保不会再次访问相同的单元格？考虑一下图上的广度优先搜索或深度优先搜索是如何工作的。
# 你应该有一个算法，其在N×N矩阵上的时间复杂度是O(N2)。如果你的算法并非如此，请考虑是否错误地计算了时间复杂度，或者是否你的算法不是最优的。
# 
# 
from typing import List
class Solution:
    #dfs
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        res = []
        def dfs(x,y):
            nonlocal area
            if (x<0 or x>= len(land) or y < 0 or y>= len(land[0]) or land[x][y] != 0):
                return
            land[x][y] = 1
            area = area + 1         #原来池塘基础上+1

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x + 1, y + 1)
            dfs(x + 1, y - 1)
            dfs(x - 1, y - 1)
            dfs(x - 1, y + 1)
            return

        for x in range(len(land)):
            for y in range(len(land[0])):
                if land[x][y] == 0:
                    area = 0            #默认0，然后dfs，得到结果放入re
                    dfs(x, y)           
                    res.append(area)
        res.sort()
        return res

land = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
o = Solution()
print(o.pondSizes(land))