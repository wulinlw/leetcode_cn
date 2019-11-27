#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/queue-stack/219/stack-and-dfs/885/
# 目标和
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
# 示例 1:
# 输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释: 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 一共有5种方法让最终目标和为3。
# 注意:
# 数组非空，且长度不会超过20。
# 初始的数组的和不会超过1000。
# 保证返回的最终结果能被32位整数存下。
# Definition for a Node.

class Solution(object):
    # 利用dfs深度优先搜索
    # 设置一个哈希表（字典），键是一个元祖，元祖第一位是目前的和，第二位是目前的位数。值是这个元祖推导到最后能有多少个解。
    # 例如d[(4,5)] = 1 代表读到4位的时候，正好有一个解符合条件（那么在这个例子中符合条件的S就是5），然后倒导d([3,5]) = 2 ......(在这种情况下，第4位是0，总共就4位)
    # 初始化节点为(0,0)，代表已经读了0位，现在和为0
    # 开始深度优先搜索，当i比位数小，说明可以深入。为了避免重复运算，要看当前节点是否在d里已经出现过。
    # 每次深入的结果，就是d[(i, cur)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i], i + 1, d)。意思就是当前节点推导到最后有多少个可能性呢？这个节点再读取一位，要么是加上这一位，要么是减掉这一位，所以这个节点的可能性就是对加上下一位的可能性与减掉下一位的可能性之和。
    # 当深入到最后一位时，再深入就超了位数限制了，此时可以直接判断这个节点的和（即元祖的第二位）是否等于需要的S。是了为1，否则为0。因为dfs可能遍历到重复节点，所以return一行写作d.get((i, cur), int(cur == S))。如果是重复节点直接返回字典里对应值就完事儿(ง •̀_•́)ง

    # 作者：jimmy00745
    # 链接：https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        d = {}
        #cur    当前位的和
        #i      第几位
        #d      遍历过的字典
        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in d: # 搜索周围节点
                # 这个节点再读取一位，要么是加上这一位，要么是减掉这一位，所以这个节点的可能性就是对加上下一位的可能性与减掉下一位的可能性之和。
                d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i],i + 1, d)
            return d.get((cur, i), int(cur == S))#get的默认值int(cur == S) 
        return dfs(0, 0, d)


nums = [1, 1, 1, 1, 1]
S = 3
ss = Solution()
re = ss.findTargetSumWays(nums,S)
print(re)






