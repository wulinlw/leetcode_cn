# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.15.珠玑妙算
# 
# https://leetcode-cn.com/problems/master-mind-lcci/
# 
# 珠玑妙算游戏（the game of master mind）的玩法如下。
# 计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。
# 给定一种颜色组合solution和一个猜测guess，编写一个方法，返回猜中和伪猜中的次数answer，其中answer[0]为猜中的次数，answer[1]为伪猜中的次数。
# 示例：
# 输入： solution="RGBY",guess="GGRR"
# 输出： [1,1]
# 解释： 猜中1次，伪猜中1次。
# 
# 提示：
# 
# len(solution) = len(guess) = 4
# solution和guess仅包含"R","G","B","Y"这4种字符
# 
# 
# 
# Easy 49.1%
# Testcase Example: "RGRB"
# "BBBY"
# 
# 提示:
# 首先尝试创建一个具有每个元素发生频率的数组。
# 为了在实现中简单明了，你可能需要使用其他方法和类。
# 
# 
from typing import List
import collections
class Solution:
    # 建立两个字典，存放solution和guess颜色出现的个数
    # 因为题目中说“猜中”不能算入“伪猜中”，因此“猜中”的优先级更高
    # 先计算猜中的次数，对应的字典-1
    # 再计算伪猜中的次数，对应的字典-1
    def masterMind(self, solution: str, guess: str) -> List[int]:
        dicts=collections.Counter(solution)
        dictg=collections.Counter(guess)
        answer=[0,0]
        for i in range(len(solution)):
            if solution[i]==guess[i]:
                answer[0]+=1
                dicts[solution[i]]-=1
                dictg[guess[i]]-=1
        for i in range(len(solution)):
            if guess[i] in solution and dicts[guess[i]]>0 and dictg[guess[i]]>0:    #都还有剩余
                answer[1]+=1
                dicts[guess[i]]-=1
                dictg[guess[i]]-=1
        return answer



solution="RGBY"
guess="GGRR"
o = Solution()
print(o.masterMind(solution, guess))