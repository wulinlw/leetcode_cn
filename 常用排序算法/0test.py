#!/usr/bin/python
#coding:utf-8
def bobble(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

def merge(nums):
    if len(nums)<=1:return nums
    mid = len(nums)//2
    return __merge(merge(nums[:mid]), merge(nums[mid:]))

def __merge(l, r):
    re = []
    while l and r:
        if l[0]<r[0]:
            re.append(l.pop(0))
        else:
            re.append(r.pop(0))
    while l:
        re.append(l.pop(0))
    while r:
        re.append(r.pop(0))
    return re

# ------------------
def quick(nums, low, high):
    if low<high:
        p = partition(nums,low,high)
        quick(nums, low, p-1)
        quick(nums, p+1, high)
    return nums

def partition(nums, low, high):
    i = low-1
    pivot = nums[high]
    for j in range(low,high):
        if nums[j]<pivot:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[high] = nums[high],nums[i+1]
    return i+1

def insert(nums):
    for i in range(len(nums)):
        pre = i-1
        cur = nums[i]
        while pre>=0 and nums[pre]>cur:
            nums[pre+1] = nums[pre]
            pre -= 1
        nums[pre+1] = cur
    return nums

def bucket(nums):
    maxval = max(nums)
    bucket = [0] *(maxval+1)
    for i in nums: 
        bucket[i] += 1
    re = []
    for i in range(len(bucket)):
        if bucket[i] != 0:
            while bucket[i]:
                re.append(i)
                bucket[i]-=1
    return re

def count(nums):
    re = [0]*len(nums)
    for i in range(len(nums)):
        c=0
        d=0
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                c+=1
            elif nums[i]==nums[j]:
                d+=1
        for k in range(c,c+d):
            re[k] = nums[i]
    return re



def select(nums):
    for i in range(len(nums)):
        idx = i
        for j in range(i,len(nums)):
            if nums[idx]>nums[j]:
                idx = j
        nums[i],nums[idx]= nums[idx],nums[i]
    return nums

def shell2(nums):
    n = len(nums)
    gap = n//2
    while gap>0:
        for i in range(len(nums)):
            j = i
            cur = nums[i]
            while j-gap>=0 and nums[j-gap]>cur:
                nums[j] = nums[j-gap]
                j-=gap
            nums[j] = cur
        gap //= 2
    return nums



def heapSort(arr): 
    def heapify(arr, n ,i):
        largest = i
        l = 2*i+1
        r = 2*i+2
        if l<n and arr[i] < arr[l]:
            largest =l
        if r<n and arr[l]<arr[r]:
            largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            heapify(arr,n,largest)

    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr, n, i)
    
    for i in range(n-1,0,-1):
        arr[0],arr[i]= arr[i],arr[0]
        heapify(arr, i , 0)
    return arr




arr = [10, 7, 8, 9, 1, 5, 5]
n = len(arr)
# re = bobble(arr)
# re = merge(arr)
# re = quick(arr, 0, n-1)#------
# re = insert(arr)#------
# re = bucket(arr)
# re = count(arr)
# re = select(arr)#-------
# re = shell2(arr)#-------
re = heapSort(arr)
# re = radix_sort(arr)
print(re)