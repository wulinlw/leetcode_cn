#!/usr/bin/python
#coding:utf-8

# 打印1到最大的n位数
# 输入数字n, 按顺序打印从1最大的n位十进制数
# 比如输入3, 则打印出1、2、3、到最大的3位数即999
class Solution:
    def Print1ToMaxOfNDigits(self, n):
        for i in range(10):
            self.recursion(str(i), n, 0)#每个数字的开头
        
    def recursion(self, s, n, index):
        if index==n-1:
            # print(s)
            self.printNum(s)
            return
        for i in range(10):
            self.recursion(s+str(i), n, index+1)

    def printNum(self, num):
        isBeginning0 = True
        nLength = len(num)
        for i in range(nLength):
            if isBeginning0 and num[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c' % num[i], end='')
        print('')

obj = Solution()
obj.Print1ToMaxOfNDigits(2)
