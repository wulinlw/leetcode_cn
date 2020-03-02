#!/usr/bin/python
#coding:utf-8

import sys,math
from typing import List
# 重点问题
# 19
# 20
# 27
# 30
# 34
# 35
# 37
# 43
# 44
# 46
# 47
# 48
# 49
# 51---------------
# 53
# 53_2
# 54
# 57_2
# 59
# 65
def bobble(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

def merge(nums):
    n = len(nums)
    if n<=1:return nums
    mid = n//2
    return _meger(merge(nums[:mid]), merge(nums[mid:]))

def _meger(l, r):
    re = []
    while l and r:
        if l[0]>r[0]:
            re.append(r.pop(0))
        else:
            re.append(l.pop(0))
    while l:
        re.append(l.pop(0))
    while r:
        re.append(r.pop(0))
    return re
    
def quick(nums, low, high):#low, high初始调用是0, len(nums)-1
    if low<high:
        pivot = partition(nums, low, high)
        quick(nums, low, pivot-1)
        quick(nums, pivot+1, high)
    return nums

def partition(nums, l, r):
    i = l-1 
    pivot = nums[r]
    for j in range(l,r):
        if nums[j] < pivot:
            i +=1 
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[r] = nums[r],nums[i+1]
    return i+1

def insert(nums):
    for i in range(len(nums)):
        pre = i-1 
        cur = nums[i]
        while  pre>=0 and nums[pre]>cur:
            nums[pre+1] = nums[pre]
            pre -= 1
        nums[pre+1] = cur
    return nums

def bucket(nums):
    bucket = [0]* (max(nums)+1)
    for i in nums:
        bucket[i] += 1
    re = []
    for i in range(len(bucket)):
        while bucket[i]>0:
            re.append(i)
            bucket[i] -= 1
    return re

def count(nums):
    re =[0]*len(nums)
    for i in range(len(nums)):
        c = 0 
        dupilicate = 0
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                c += 1
            elif nums[i]==nums[j]:
                dupilicate += 1
        for k in range(c, c+dupilicate):
            re[k] = nums[i]
    return re

def select(nums):
    for i in range(len(nums)):
        idx = i 
        for j in range(i+1, len(nums)):
            if nums[idx] > nums[j]:
                idx = j 
        nums[idx],nums[i] = nums[i],nums[idx]
    return nums

def shell2(nums):
    gap = n//2
    while gap>0:
        for i in range(len(nums)):
            pre = i
            cur = nums[i]
            if pre-gap>=00 and nums[pre-gap]>cur:
                nums[pre] = nums[pre-gap]
                pre -= gap 
            nums[pre] = cur
        gap //=2 
    return nums

def heapSort(arr): 
    def heapify(arr, n ,i):
        largest = i
        l = 2*i+1 
        r = 2*i+2 
        if l<n and arr[i]<arr[l]:
            largest = l 
        if r<n and arr[largest] < arr[r]:
            largest = r 
        if largest !=i:
            arr[largest],arr[i] = arr[i], arr[largest]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr, n , i)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


arr = [10, 7, 8, 9, 1, 5,5]
n = len(arr)
# re = bobble(arr)
# re = merge(arr)
# re = quick(arr, 0, n-1)
# re = insert(arr)
# re = bucket(arr)
# re = count(arr)
# re = select(arr)
# re = shell2(arr)
re = heapSort(arr)
print(re)
