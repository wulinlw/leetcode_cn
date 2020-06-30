#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# https://leetcode-cn.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (53.74%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 17.4K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 
# update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
# 
# 示例:
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# 说明:
# 
# 
# 数组仅可以在 update 函数下进行修改。
# 你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。
# 
# 
#
from typing import List
# @lc code=start
class NumArray:
    #线段树
    # tree[i] = tree[i * 2] + tree[i * 2 + 1];
    # 构造线段树
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.arr= [0] * (n * 2)
        # self.arr = [0] * n + nums                         #第一个for的简写
        for i in range(n, 2*n):                             #后半段填充原数组
            self.arr[i] = nums[i-n]
        for i in range(n-1, 0, -1):                         #从底层到上层，父节点 = 左 + 右
            self.arr[i] = self.arr[2*i] + self.arr[2*i + 1]
        # print(self.arr)

    def update(self, i: int, val: int) -> None:
        idx = i + self.n
        self.arr[idx] = val
        while idx > 1:
            l, r = idx, idx
            if idx % 2 == 0:                                #找左右子树索引，分别是2i,2i+1,如果idx是左节点，那r就是右节点 idx+1
                r = idx + 1
            else:
                l = idx - 1
            self.arr[idx // 2] = self.arr[l] + self.arr[r]
            idx //= 2                                       #找到父节点，更新父节点
        # print(self.arr)

    def sumRange(self, l: int, r: int) -> int:
        l += self.n                                         #在后半段中找到叶子节点的左右索引
        r += self.n
        sum = 0
        while l <= r:
            if l % 2 == 1:                                  #l是其父亲的右儿子，r是父亲的左儿子  
                sum += self.arr[l]                          #就立刻把自己加上，因为查询区间没有覆盖父亲，只覆盖了自己。
                l += 1
            if r % 2 == 0:
                sum += self.arr[r]
                r -= 1
            l //= 2                                         #找到left和right的父亲节点
            r //= 2
        return sum

# @lc code=end

# Your NumArray object will be instantiated and called as such:
nums = [2,4,5,7,8,9]
obj = NumArray(nums)
obj.update(2, 1)
print(obj.sumRange(2, 3))
