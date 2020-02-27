#!/usr/bin/python
#coding:utf-8

# 打印1到最大的n位数
# 输入数字n, 按顺序打印从1最大的n位十进制数
# 比如输入3, 则打印出1、2、3、到最大的3位数即999
class Solution:
    def Print1ToMaxOfNDigits(self, n):
        for i in range(10):                         #套路写法，生产每一位的0-9，从最左边开始生成
            self.recursion(str(i), n, 0)            #每个数字的开头
        
    # s     数字开头
    # n     几位数
    # index 当前第几位
    def recursion(self, s, n, index):
        if index==n-1:                              #达到位数，开始输出
            # print(s)
            self.printNum(s)
            return
        for i in range(10):                         #和上面一样套路，生成下一位的数0-9
            self.recursion(s+str(i), n, index+1)

    def printNum(self, num):
        isBeginning0 = True
        nLength = len(num)
        for i in range(nLength):
            if isBeginning0 and num[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%s' % num[i], end='')        #格式化字符及其ASCII码
        print('')

obj = Solution()
obj.Print1ToMaxOfNDigits(2)
