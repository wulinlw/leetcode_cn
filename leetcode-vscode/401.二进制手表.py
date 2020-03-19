#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
# https://leetcode-cn.com/problems/binary-watch/description/
#
# algorithms
# Easy (51.76%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 22.3K
# Testcase Example:  '0'
#
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
# 
# 每个 LED 代表一个 0 或 1，最低位在右侧。
# 
# 
# 
# 例如，上面的二进制手表读取 “3:25”。
# 
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
# 
# 案例:
# 
# 
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
# "0:32"]
# 
# 
# 
# 注意事项:
# 
# 
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def readBinaryWatch(self, num):
        self.result_all = []
        self.nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]        #前4个是小时，后面是分钟
        self.visited = [0]*len(self.nums)
        self.dfs(num, 0, 0)
        return self.result_all
    
    #idx计数，亮灯数
    #start，起始位置，从这里亮灯
    def dfs(self, num, idx, start):
        if idx == num:                                      #亮灯数够了
            self.result_all.append(self.handle_date(self.visited))
            return
        for i in range(start, len(self.nums)):
            self.visited[i] = 1
            if not self.calc_sum(self.visited):             #时间是否合法
                self.visited[i] = 0                         #不合法剪枝
                continue
            self.dfs(num, idx + 1, i + 1)
            self.visited[i] = 0                             #回溯
        return

    #计算时间，看看是否合法
    def calc_sum(self, visited):
        sum_h = 0                       #小时
        sum_m = 0                       #分钟
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:                   
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        return 0 <= sum_h <= 11 and 0 <= sum_m <= 59
    
    #计算时间，并返回正确时间字符串
    def handle_date(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        result = "" + str(sum_h) + ":"
        if sum_m < 10:
            result += "0" + str(sum_m)
        else:
            result += str(sum_m)
        return result
        
# @lc code=end

o = Solution()
print(o.readBinaryWatch(1))