#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/112/
# 快乐数
# 编写一个算法来判断一个数是不是“快乐数”。
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

# 示例: 
# 输入: 19
# 输出: true
# 解释: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# http://www.cnblogs.com/bozhou/p/6956324.html
# http://www.cnblogs.com/grandyang/p/4447233.html
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1. 结果为1则为true; 
        # 2. 结果无限循环，这就需要保存计算过的值，当然是使用散列表实现的字典。这里如果使用递归的话很难维护字典，所以最后改为递推。
        record = []
        sq_sum = 0
        se_n = n

        while se_n != 1:
            sq_sum = 0
            while se_n > 0:#计算这个数的所有位的平方之和
                sq_sum += (se_n % 10) * (se_n % 10) #最后一位的平方
                se_n = se_n / 10 #各位以上的所有位
            #结果存在record就说明有循环
            if sq_sum in record:
                return False
            record.append(sq_sum)
            se_n = sq_sum
        return True

    #只有4才是false
    def isHappy2(self, n):
        # Write your code here
        if n is None: return False
         
        while n != 1 and n != 4:
            nums = list(str(n))
            n = 0
            for i in nums:
                n += int(i)**2
        # 循环结束，返回结果
        if n == 1: return True
        if n == 4: return False

nums = 9
s = Solution()
n = s.isHappy(nums)
print(n)










