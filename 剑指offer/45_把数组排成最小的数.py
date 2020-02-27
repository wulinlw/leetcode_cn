#!/usr/bin/python
#coding:utf-8

# // 面试题45：把数组排成最小的数
# // 题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼
# // 接出的所有数字中最小的一个。例如输入数组{3, 32, 321}，则打印出这3个数
# // 字能排成的最小数字321323。
class Solution:
    def PrintMinNumber(self, nums):
        if len(nums) == 0:
            return 0
        numstr = [str(i) for i in nums]
        #字符排序，相同位小的排前面，长的排前面
        #冒泡排序
        for i in range(len(numstr)):
            for j in range(i+1,len(numstr)):
                a = int(numstr[i]+numstr[j])
                b = int(numstr[j]+numstr[i])
                if a>b: 
                    numstr[i],numstr[j] = numstr[j],numstr[i]
        print(numstr)
        return ''.join(numstr)
    
class Compare(str):
    def __lt__(x, y):
        return x + y < y + x

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=Compare)
        return ''.join(nums)
nums = [3,32,321]
nums = [3,30,34,5,9]
obj = Solution()
print(obj.PrintMinNumber(nums))
