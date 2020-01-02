#!/usr/bin/python
#coding:utf-8

# 二进制中1 的个数
# 请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。
# 举例说明
# 例如，把9表示成二进制是1001，有2位是1。因此如果输入9，则该函数输出2。
class Solution:
    def numberOf1(self, n):
        #
        # 1100  n
        # 1011  n-1
        # 1000  (n-1) & n
        # 相当于n的最右边的1变成0，（这个例子看n的左边第二位）
        cnt = 0
        while n:
            cnt += 1
            n = (n-1) & n
        return cnt


    def numberOf1_1(self, n):
        # 右移不支持负数，负数最高位是1，右移后为保证是负数，会自动往最左边放1
        cnt = 0
        f = 1
        while n:
            cnt += n&f
            n = n>>1
        return cnt
    
    def numberOf1_2(self, n):
        cnt = 0
        f = 1
        while f:
            if n&f:
                cnt += 1
            f = f<<1
        return cnt
    
    # 判断两个数的二进制表示有多少位不一样, 直接比较两个数的二进制异或就可以
    def andOr(self, m, n):
        diff = m^n
        count = 0
        while diff:
            count += 1
            diff = diff&(diff-1)
        return count

obj = Solution()
print(obj.numberOf1(9))
# print(obj.numberOf1(-1))
