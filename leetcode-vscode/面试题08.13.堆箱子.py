#!/usr/bin/python
#coding:utf-8

# 面试题08.13.堆箱子
# 堆箱子。给你一堆n个箱子，箱子宽 wi、高hi、深di。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。实现一种方法，搭出最高的一堆箱子。
# 箱堆的高度为每个箱子高度的总和。

# 输入使用数组[wi, di, hi]表示每个箱子。

# 示例1:
#  输入：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#  输出：6

# 示例2:
#  输入：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
#  输出：10
# 提示:

# 箱子的数目不大于3000个。
# https://leetcode-cn.com/problems/pile-box-lcci/

from typing import List
class Solution:
    # 最长上升子序列，类似的变化题目还有信封问题、俄罗斯套娃问题，大同小异
    def pileBox(self, box: List[List[int]]) -> int:
        dp = [0 for _ in range(len(box))]
        box.sort()

        for i in range(len(box)):
            dp[i] = box[i][2]
            for j in range(i):
                if box[j][0] < box[i][0] and box[j][1] < box[i][1] and box[j][2] < box[i][2]:
                    dp[i] = max(dp[i], dp[j] + box[i][2])
        return max(dp)






box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
o = Solution()
print(o.pileBox(box))