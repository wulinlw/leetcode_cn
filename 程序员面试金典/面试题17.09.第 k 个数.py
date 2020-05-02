# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.09.第 k 个数
# 
# https://leetcode-cn.com/problems/get-kth-magic-number-lcci/
# 
# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
# 示例 1:
# 
# 输入: k = 5
# 
# 输出: 9
# 
# 
# 
# Medium 52.9%
# Testcase Example: 1
# 
# 提示:
# 明确这个问题的要求。要求满足 3a× 5b× 7c 这一形式的第 k 小的值。
# 蛮力解法得到的形如 3a× 5b × 7c 的第 k 小的值是什么样的?
# 在寻找 3a × 5b × 7c 的第 k 个最小值时，我们知道 a、b、c 将小于等于 k。你能生成所有可能的数字吗?
# 查看 3a×5b×7c 对应的所有值的列表，可以观察到列表中的每个值都是 3×(列表中前面的某值)、5×(列表中前面的某值)或 7×(列表中前面的某值)。
# 由于每个数字都是列表中先前值的 3 倍、5 倍或 7 倍，因此我们可以检查所有可能的值，然后选择下一个还没有看到的值。这将导致许多重复的工作。如何才能避免这种情况呢?
# 不要检查列表中的所有值来寻找下一个值(通过将每个值乘以 3、5、7)，而是这样考虑:当你将一个值 x 插入列表时，可以“构造”3x、5x 和 7x 以供以后使用。
# 当你将 x 添加到前 k 个值的列表中时，可以将 3x、5x 和 7x 添加到新的列表中。如何使其尽可能地优化?保留多个队列如何?总是需要插入 3x、5x 和 7x 吗? 或者，有时你只需要插入 7x?你需要避免相同的数字出现两次。
# 
# 

class Solution:
    # 丑数变种
    def getKthMagicNumber(self, k: int) -> int:
        res = [1] * k
        idx3, idx5, idx7 = 0, 0, 0
        for i in range(1, k):
            res[i] = min(res[idx3]*3, res[idx5]*5, res[idx7]*7)
            if res[i] == res[idx3]*3: idx3 += 1
            if res[i] == res[idx5]*5: idx5 += 1
            if res[i] == res[idx7]*7: idx7 += 1
        return res[k-1]


k = 5
o = Solution()
print(o.getKthMagicNumber(k))