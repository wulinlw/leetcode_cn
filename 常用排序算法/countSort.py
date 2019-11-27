#!/usr/bin/python
#coding:utf-8

#计数排序
def countSort(arr):
    n = len(arr)
    res = [None] * n
    for i in range(n):
        p = 0
        for j in range(n):
            if arr[i] > arr[j]:
                p += 1
        res[p] = arr[i]
    return res

arr = [1,2,5,3,4]
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
re = countSort(arr)
print(re)