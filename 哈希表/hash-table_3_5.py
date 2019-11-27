#!/usr/bin/python
# coding:utf-8

# https://leetcode-cn.com/explore/learn/card/hash-table/205/practical-application-hash-map/813/
# 两个列表的最小索引总和
# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

# 示例 1:
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
# 示例 2:

# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
# 提示:

# 两个列表的长度范围都在[1, 1000]内。
# 两个列表中的字符串的长度将在[1，30]的范围内。
# 下标从0开始，到列表的长度减1。
# 两个列表都没有重复的元素。


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        map1 = {list1[i]: i for i in range(len(list1))}  # 转换hash
        map2 = {list2[i]: i for i in range(len(list2))}  # 转换hash
        inter = set(list1) & set(list2)  # 求交集
        sum_index = {i: map1[i] + map2[i] for i in inter}  # 交集成员索引求和
        # 找最少的索引和的成员
        # return [val for val in inter if sum_index[val] == min(sum_index.values())]
        res = []
        for val in inter:
            if sum_index[val] == min(sum_index.values()):
                res.append(val)
        return res


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines",
         "Hungry Hunter Steakhouse", "Shogun"]
obj = Solution()
res = obj.findRestaurant(list1, list2)
print(res)
