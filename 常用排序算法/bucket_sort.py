#!/usr/bin/python
#coding:utf-8

#桶排序1
def bucket_sort(lst):
    buckets = [0] * ((max(lst) - min(lst))+1)
    for i in range(len(lst)):
        buckets[lst[i]-min(lst)] += 1
    res=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(lst)]*buckets[i]
    return res
#桶排序2
def buketSort(nums):
    # 选择一个最大的数
    max_num = max(nums)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0]*(max_num+1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in nums:
        bucket[i] += 1
    print(bucket)
    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            # for y in range(bucket[j]):
            sort_nums.append(j)

    return sort_nums


arr = [1,2,5,3,4]
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
re = buketSort(arr)
print(re)