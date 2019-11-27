#!/usr/bin/python
#coding:utf-8

# 快速排序
def partition(arr,low,high):
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]    
 
    for j in range(low , high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
        # print(i,arr)
    arr[i+1],arr[high] = arr[high],arr[i+1]#交换下i+1he结尾，用于下次基准比较
    # print(arr)
    return ( i+1 )
 
# 快速排序函数
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

arr = [1,2,5,3,4]
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
re = quickSort(arr,0,n-1)
print(re)