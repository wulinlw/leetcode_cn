# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.01.交换数字
# 
# https://leetcode-cn.com/problems/swap-numbers-lcci/
# 
# 编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。
# 示例：
# 输入: numbers = [1,2]
# 输出: [2,1]
# 
# 提示：
# 
# numbers.length == 2
# 
# 
# 
# Medium 81.8%
# Testcase Example: [0,2147483647]
# 
# 提示:
# 尝试在数轴上画出a和b两个数字。
# 定义diff为a和b之间的差。你能以某种方式使用diff吗？那么你能去掉这个临时变量吗？
# 你也可以尝试使用XOR。
# 
# 
from typing import List
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[0] ^ numbers[1]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers

numbers = [1,2]
o = Solution()
print(o.swapNumbers(numbers))
