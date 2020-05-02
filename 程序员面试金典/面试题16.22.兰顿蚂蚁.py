# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.22.兰顿蚂蚁
# 
# https://leetcode-cn.com/problems/langtons-ant-lcci/
# 
# 一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。
# (1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。
# (2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。
# 
# 编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。
# 
# 网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 &#39;X&#39; 表示，白色方格由 &#39;_&#39; 表示，蚂蚁所在的位置由 &#39;L&#39;, &#39;U&#39;, &#39;R&#39;, &#39;D&#39; 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。
# 
# 示例 1:
# 
# 输入: 0
# 输出: ["R"]
# 
# 
# 示例 2:
# 
# 输入: 2
# 输出:
# [
#   "_X",
#   "LX"
# ]
# 
# 
# 示例 3:
# 
# 输入: 5
# 输出:
# [
#   "_U",
#   "X_",
#   "XX"
# ]
# 
# 
# 说明：
# 
# 
# 	K <= 100000
# 
# 
# 
# Medium 51.2%
# Testcase Example: 0
# 
# 提示:
# 棘手的是处理无限网格。你有什么选择？
# 选项1：你真的需要一个无线的网络吗？再次审题。你知道网格的最大尺寸吗？
# 选项 2：想想ArrayList的工作原理。它能派上用场吗？
# 选项2：使用ArrayList是不可能的，因为那样太烦琐了。也许构建自己的列表会更容易，但要专门针对矩阵。
# 方法2：一种方法是当蚂蚁到达边缘时，将数组的大小加倍。但是，你将如何处理蚂蚁到达负坐标的问题呢？数组不能有负的索引。
# 选项2：注意，问题中没有规定坐标的标签必须保持不变。你能把蚂蚁和所有的单元格信息移动到正坐标吗？换句话说，如果当你需要让数组n向负方向增长时，你重新标记了所有的指标使它们仍然是正的，会发生什么?
# 选项3：另一件需要考虑的事情是，你是否真的需要一个网格来实现它。在这个问题中你真正需要什么信息?
# 选项3：你实际上需要的是来查看一个单元格是白色的还是黑色的某种方式（当然还有蚂蚁的位置）。你能把所有的白色方格存在一个链表中吗?
# 选项3：你可以考虑维护一个所有白色方格的散列集合。不过，你怎么才能打印出整个网格呢?
# 
# 
from typing import List
class Solution:
    def printKMoves(self, K: int) -> List[str]:
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        black = set()
        pos, curr_dir = (0, 0), 2
        # 模拟 K 步骤
        for i in range(K):
            if pos in black:
                curr_dir = (curr_dir - 1) % 4
                black.remove(pos)
            else:
                curr_dir = (curr_dir + 1) % 4
                black.add(pos)
            pos = (pos[0] + dirs[curr_dir][0], pos[1] + dirs[curr_dir][1])
            
        all_x = [x for x, _ in black] + [pos[0]]
        all_y = [y for _, y in black] + [pos[1]]
        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)
        # 初始化矩阵为全白
        matrix = [["_" for _ in range(min_y, max_y + 1)] for _ in range(min_x, max_x + 1)]
        # 填充黑色
        for x, y in black:
            matrix[x - min_x][y - min_y] = "X"
        # 填充方向
        matrix[pos[0] - min_x][pos[1] - min_y] = ["L", "U", "R", "D"][curr_dir]
        
        for i in range(len(matrix)):
            matrix[i] = "".join(matrix[i])
        return matrix

k = 2
o = Solution()
print(o.printKMoves(k))