#!/usr/bin/python
#coding:utf-8

# // 面试题43：从1到n整数中1出现的次数
# // 题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。例如
# // 输入12，从1到12这些整数中包含1 的数字有1，10，11和12，1一共出现了5次。

class Solution:
    def NumberOf1Between1AndN_Solution(self,n):
        # write code here
        res = 0
        i = 1  # 个位开始
        while n // i != 0:
            high = n//(i*10) # 高位数
            current = (n//i) % 10  # 第i位数
            low = n - (n//i) * i  # 低位数
            if current == 0:
                res += high * i
            elif current == 1:
                res += high * i + low + 1
            else:
                res += (high+1) * i
            i *= 10
        return res

    #书上的，
    def NumberOf1Between1AndN(self, nums):
        nums = str(nums)
        n = len(nums)
        first = int(nums[0])
        if n==1 and first==0:
            return 0
        if n==1 and first>0:        #个位数中，只有一个1
            return 1

        # // 假设strN是"21345"
        # // numFirstDigit是数字10000-19999的第一个位中1的数目
        if first>1:
            begin1 = pow(10, n-1)
        elif first==1:
            begin1 = int(nums[1:])+1
        
        # // numOtherDigits是01346-21345除了第一位之外的数位中1的数目
        other1 = first * (n-1) * pow(10, n-2)
        # print(nums,begin1 , other1)
        # // numRecursive是1-1345中1的数目
        recursion1 = self.NumberOf1Between1AndN(int(nums[1:]))

        return begin1 + other1 + recursion1
        
    def test(self, num):
        # 常规方法用来比较
        ret = 0
        for n in range(1, num+1):
            for s in str(n):
                if s == '1':
                    ret += 1
        return ret
n=21345

obj = Solution()
print(obj.test(n))
print(obj.NumberOf1Between1AndN(n))

