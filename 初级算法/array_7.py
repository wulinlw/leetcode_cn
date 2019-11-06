#!/usr/bin/python
#coding:utf-8
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


nums = [1, 2, 3]
nums = [4, 3, 2, 9]
# nums = [0]
# nums = [9]
s = Solution()
n = s.plusOne(nums)
print('return', n)
