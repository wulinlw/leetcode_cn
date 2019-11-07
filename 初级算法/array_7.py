#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/27/
# 加一
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:

# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        正序计算
        """
        digits = digits[::-1]
        print(digits)
        l = len(digits)
        p = l - 1
        f = False
        while (p >= 0):
            if digits[p] != 9:
                digits[p] += 1
                if (f == True) or (p == l - 1):
                    return digits
            else:
                f = True
                digits[p] = 0
                p -= 1
                if p == -1:
                    digits.insert(0, 1)
                    return digits

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        反转数组，从左往右计算
        反转后第一位+1小于10，则+1即可退出循环
        反转后第一位+1=10，则当前位=0，继续循环；最后一位时直接=0且最后增加一位1
        """
        length = len(digits)
        digits = digits[::-1]

        for i in range(length):
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                break
            elif i != length - 1:
                digits[i] = 0
            else:
                digits[i] = 0
                digits.append(1)

        digits = digits[::-1]
        return digits

    def plusOne3(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        类型转换的方法
        """
        s = ''
        for i in digits:
            s += str(i)
        s = int(s)
        s += 1
        s = str(s)
        digits = []
        for i in s:
            digits.append(int(i))
        return digits


nums = [1, 2, 3]#321
nums = [4, 3, 2, 9]#9234 ，0234，  4330
# nums = [0]
# nums = [9]
s = Solution()
n = s.plusOne2(nums)
print('return', n)
