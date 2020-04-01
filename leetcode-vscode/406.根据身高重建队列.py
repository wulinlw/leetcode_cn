#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (62.74%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    21.8K
# Total Submissions: 34.2K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
# 
# 注意：
# 总人数少于1100人。
# 
# 示例
# 
# 
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # you题意可知
    # 身高越高的人，前面比他高的人数，就是当前队列的索引。比如上述people->[[7,0] [7,1]]
    # 如果比他(身高最高的人)矮的人，如[5,0]，前面比他高的人-0，应是当前插入队列索引下前面的一个数，如[[5,0]，[7,0] [7,1]]
    # 因此总结规律如下：
    # 1. 队列应从身高降序排列。如果身高相同者，升序排序
    # 然后依次遍历，按当前比他高身高人数为索引插入新建队列
    # 注意，身高最高者，他的索引"必定"有0，并列才有1，意味着(身高比他矮的，且索引相同时，必定在他前面)
    # 因此从身高降序排列，不会影响身高矮插入队列是，出现队列乱序的错误。
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0], x[1]))
        # print(people)
        re = []
        for p in people:
            re.insert(p[1], p)
        return re

# @lc code=end
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

o = Solution()
print(o.reconstructQueue(people))
