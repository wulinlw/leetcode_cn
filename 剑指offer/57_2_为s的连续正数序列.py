#!/usr/bin/python
#coding:utf-8

# // 面试题57（二）：和为s的连续正数序列
# // 题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
# // 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、
# // 4～6和7～8。


class Solution:
    def FindContinuousSequence(self, n):
        if n <3:return False
        small = 1
        big = 2
        mid = (1+n)//2
        curSum = small + big                        #滑动窗口的累加值
        while small < mid:                          #只需要走到一半即可，n+n+1 > 2n
            if curSum == n:                         
                self.printSequence(small, big)
            
            while curSum>n and small<mid:           #滑动窗口累加值大于目标n，需要把左边向右移动一位
                curSum -= small                     
                small += 1
                if curSum == n:                     #移位后再对比一次
                    self.printSequence(small, big)
            big += 1                                #滑动窗口sum小于目标n，向右滑动1位
            curSum += big                           #滑动后累加窗口sum

            # 这样理解更简单
            # if cursum > n:
            #     cursum -= small
            #     small +=1
            # else:
            #     big += 1
            #     cursum += big
    
    def printSequence(self, small, big):
        for i in range(small, big+1):
            print(i, end=",")
        print("\n")
        

        
n = 18
obj = Solution()
print(obj.FindContinuousSequence(n))
