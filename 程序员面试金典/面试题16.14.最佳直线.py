# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.14.最佳直线
# 
# https://leetcode-cn.com/problems/best-line-lcci/
# 
# 给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。
# 设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。
# 示例：
# 输入： [[0,0],[1,1],[1,0],[2,0]]
# 输出： [0,2]
# 解释： 所求直线穿过的3个点的编号为[0,2,3]
# 
# 提示：
# 
# 2 
# len(Points[i]) = 2
# 
# 
# 
# Medium 50.6%
# Testcase Example: [[-38935,27124],[-39837,19604],[-7086,42194],[-11571,-23257],[115,-23257],[20229,5976],[24653,-18488],[11017,21043],[-9353,16550],[-47076,15237],[-36686,42194],[-17704,1104],[31067,7368],[-20882,42194],[-19107,-10597],[-14898,24506],[-20801,42194],[-52268,40727],[-14042,42194],[-23254,42194],[-30837,-53882],[1402,801],[-33961,-984],[-6411,42194],[-12210,22901],[-8213,-19441],[-26939,20810],[30656,-23257],[-27195,21649],[-33780,2717],[23617,27018],[12266,3608]]
# 
# 提示:
# 有时，蛮力解法是相当好的办法。你能试试所有可能的直线吗？
# 你不能真的试遍世界上所有可能的无限长的线。但你知道一条“最好”的线必须至少相交两点。你能连接每对点吗？你可以检查每一条线是否是最优的吗？
# 你应该能得到O(N²)的解法。
# 你试过使用散列表吗?
# 
# 
from typing import List
class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        from collections import OrderedDict
        lines = OrderedDict()
        for i, p_i in enumerate(points):
            for j in range(i+1, len(points)):
                p_j = points[j]
                lines[(i, j)] = 2
                for k in range(j+1, len(points)):
                    p_k = points[k]
                    if (p_k[0]-p_i[0])*(p_k[1]-p_j[1]) == (p_k[1]-p_i[1])*(p_k[0]-p_j[0]):
                        lines[(i, j)] += 1
        max_value = max(lines.values())
        # print(lines)
        for i in lines.keys():
            if lines[i] == max_value:
                return [i[0], i[1]]


o = Solution()
print(o.bestLine(points))