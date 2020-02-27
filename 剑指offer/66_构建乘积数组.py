#!/usr/bin/python
#coding:utf-8

# // 面试题66：构建乘积数组
# // 题目：给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其
# // 中B中的元素B[i] =A[0]×A[1]×…×A[i-1] × A[i+1]×…×A[n-1]。不能使用除法。
from tpye import List
class Solution(object):
    # 构造的B，第i位是：前面的乘积*后面的乘积，不包含i，
    # 如果能用除法，就用所有的乘积除以i即可
    # 思路：
    # 1、计算i前面的乘积
    # 2、计算i后面的乘积
    # 3、1*2即可
    def BuildProductionArray(self, nums):
        n = len(nums)
        if n==0:return False
        out = [1] * n
        for i in range(1,n):                #计算的i前面的乘积
            out[i] = out[i-1] * nums[i-1]   #每一步使用上一步的值*nums的下一位即可
        # print(out)
        
        tmp = 1                             #计算的i后面的乘积
        for j in range(n-2, -1, -1):        #倒着乘，每一步使用上一步的结果
            tmp *= nums[j+1]                #这里是j+1,避免越界，所以上面是n-2
            out[j] *= tmp
        return out

    #看这个
    def constructArr(self, a: List[int]) -> List[int]:
        res = [1 for i in range(len(a))]
        left = 1
        for i in range(len(res)):
            res[i] = left
            left *= a[i]

        right = 1
        for i in range(len(res)-1,-1,-1):
            res[i] *= right
            right *= a[i]
            
        return res

# 作者：zhu-230
# 链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/python3shuang-bai-by-zhu-230/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
num = [1,2,3,4,5]
S = Solution()
print(S.constructArr(num))

