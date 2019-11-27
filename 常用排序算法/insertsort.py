#!/usr/bin/python
#coding:utf-8

#插入排序
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        # print(arr[preIndex] ,current)
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]#后移一位
            preIndex-=1
        # print(arr)
        arr[preIndex+1] = current
        # print(arr)
    return arr


nums = [5,4,3,2,1]
re = insertionSort(nums)
print(re)