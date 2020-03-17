#
# @lc app=leetcode.cn id=1291 lang=python3
#
# [1291] 顺次数
#
# https://leetcode-cn.com/problems/sequential-digits/description/
#
# algorithms
# Medium (46.53%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 5.5K
# Testcase Example:  '100\n300'
#
# 我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
# 
# 请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。
# 
# 
# 
# 示例 1：
# 
# 输出：low = 100, high = 300
# 输出：[123,234]
# 
# 
# 示例 2：
# 
# 输出：low = 1000, high = 13000
# 输出：[1234,2345,3456,4567,5678,6789,12345]
# 
# 
# 
# 
# 提示：
# 
# 
# 10 <= low <= high <= 10^9
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 利用回溯生产 123类型的连续数。
    # 加一个内循环生产 123、234等同位数的
    # 加一个外循环生产 123、1234等不同位数的
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def dfs(val, digit):
            val = val * 10 + digit          
            if(val > high): 
                return
            if(val <= high and val >= low): #符合范围的加入结果集
                self.res.append(val)
            if(digit < 9):
                dfs(val, digit+1)           #下一位+1

        self.res = []
        for i in range(1,10):               #1-9
            dfs(0, i)                       #初始值0，第一位从1开始
        self.res.sort()                     #结果要排序输出
        return self.res

    

    # 123456789，按始末数字长度滑窗判断    
    # Time: O(1), Space: O(1)
    def sequentialDigits2(self, low, high):
        ans = []
        min, max = len(str(low)), len(str(high))
        s = '123456789'

        while min <= max:                   # 窗口大小
            for i in range(9-min+1):        # 防止越界，左窗口最后能到的索引
                temp = int(s[i:i+min])      # 窗口范围值，每次都是短窗口长度
                if temp >= low and temp <= high:
                    ans.append(temp)
            min += 1                        #左窗口移动
        return ans
    


# @lc code=end

low = 100
high = 300
o = Solution()
print(o.sequentialDigits(low, high))
