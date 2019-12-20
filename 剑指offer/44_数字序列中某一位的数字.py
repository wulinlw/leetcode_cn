#!/usr/bin/python
#coding:utf-8

# // 面试题44：数字序列中某一位的数字
# // 题目：数字以0123456789101112131415…的格式序列化到一个字符序列中。在这
# // 个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一
# // 个函数求任意位对应的数字。
class Solution:
    def digitAtIndex(self, index):
        if index < 0:
            return -1
        digits = 1
        while True:
            length = self.digitsLength(digits)          #n位数的长度
            if index < length*digits:                   #长度在n位数的范围内
                return self.findIndex(index, digits)
            index -= length*digits                      #超过了这个长度，减去已知的长度
            digits += 1

    # 计算n位数有多少个 ，1-10 2-90 3-900 4-9000
    def digitsLength(self, digits):
        if digits==1:
            return 10
        c = pow(10, digits-1)
        return 9 * c
    
    # 从第n位中找出index的位数
    def findIndex(self, index, digits):
        first = 0
        if index==1:
            first = 0
        else:
            first = pow(10, digits-1)           #n位数的第一个数
        num = first + index//digits             #位数除以长度=第xx位数
        return str(num)[index % digits]         #第xx位数中找到需要的数
        # indexFromRight = digits - index % digits
        # for _ in range(1,indexFromRight):
        #     num = num//10
        # return num % 10


obj = Solution()
print(obj.digitAtIndex(1000))
print(obj.digitAtIndex(1001))
print(obj.digitAtIndex(1002))
print(obj.digitAtIndex(1003))
print(obj.digitAtIndex(1004))
print(obj.digitAtIndex(1005))
