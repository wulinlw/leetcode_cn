#!/usr/bin/python
#coding:utf-8

# 面试题 17.08. 马戏团人塔
# 有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

# 示例：

# 输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
# 输出：6
# 解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
# 提示：

# height.length == weight.length <= 10000
# https://leetcode-cn.com/problems/circus-tower-lcci/

from typing import List
class Solution:
    # 俄罗斯套娃信封问题
    # https://leetcode-cn.com/problems/circus-tower-lcci/solution/python-solutiontan-xin-er-fen-cha-zhao-by-gareth/
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        if not height: return 0
        length = len(height)
        actors = [(height[i], weight[i]) for i in range(length)]
        actors.sort(key=lambda x:(x[0], -x[1]))                     #升序排序身高，若身高相同，体重按降序排序。
        # print(actors)

        tail = [actors[0][1]]                                       #记录符合条件的（体重）
        for i in range(1, len(actors)):
            if actors[i][1] > tail[-1]:                             #比数组中最后一个大直接加入
                tail.append(actors[i][1])
                continue
        
            left, right = 0, len(tail)-1                            #二分法，找到当前值插入的位置
            while left < right:                                     #也可以用单调栈排列法做，这里会超时
                mid = (left + right)>>1                             #也可以用bisect找插入点
                if tail[mid] < actors[i][1]: 
                    left = mid + 1
                else:
                    right = mid
            tail[left] = actors[i][1]                               #把这个位置的值更新为新的数据
        return len(tail)


height = [65,70,56,75,60,68] 
weight = [100,150,90,190,95,110]

height = [2868,5485,1356,1306,6017,8941,7535,4941,6331,6181]
weight = [5042,3995,7985,1651,5991,7036,9391,428,7561,8594]
o = Solution()
print(o.bestSeqAtIndex(height, weight))
# print(o.numberOf2sInRange2(1125))






