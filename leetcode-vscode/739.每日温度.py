#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (58.66%)
# Likes:    363
# Dislikes: 0
# Total Accepted:    60.6K
# Total Submissions: 97.2K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
# 
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4,
# 2, 1, 1, 0, 0]。
# 
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
# 
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:    #当前>栈顶，则弹出栈顶(小的idx)并计算距离
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)                         #记录索引

        return res
        
# @lc code=end

nums = [73,74,75,71,69,72,76,73]
o = Solution()
print(o.dailyTemperatures(nums))