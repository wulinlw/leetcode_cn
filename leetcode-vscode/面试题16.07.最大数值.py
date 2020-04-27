# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.07.最大数值
# 
# https://leetcode-cn.com/problems/maximum-lcci/
# 
# 编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。
# 示例：
# 输入： a = 1, b = 2
# 输出： 2
# 
# 
# 
# Easy 71.8%
# Testcase Example: 2147483647
# -2147483648
# 
# 提示:
# 如果a > b，则k为1，否则为0。如果给定k，你能返回最大值吗（没有比较或if-else逻辑）？
# 如果当a > b时，k等于1，那么当k等于0时则相反，然后你可以返回a*k + b* (非k)。但你如何创建k？
# 当a > b时，a – b > 0。你能得到a – b的符号位吗？
# 你考虑过如何处理a – b中的整数溢出吗？
# 
# 

class Solution:
    # max(a, b) = ((a + b) + abs(a - b)) / 2
    def maximum(self, a: int, b: int) -> int:
        sum = a+b
        dif = a-b
        return (sum + abs(dif))//2
        
a=1
b=2
o = Solution()
print(o.maximum(a,b))