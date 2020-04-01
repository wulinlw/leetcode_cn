#!/usr/bin/python
#coding:utf-8
# O(n2)
def bobble(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

# O(nlog2n)
def merge(nums):
    n = len(nums)
    if n<=1:
        return nums
    mid = n//2
    L = nums[:mid]
    R = nums[mid:]
    return _merge(merge(L), merge(R))

def _merge(l, r):
    re = []
    while l and r:
        if l[0] < r[0]:
            re.append(l.pop(0))
        else:
            re.append(r.pop(0))
    while l:
        re.append(l.pop(0))
    while r:
        re.append(r.pop(0))
    return re    

# O(nlog2n)
def quick(nums, low, high):#low, high初始调用是0, len(nums)-1
    if low < high:
        p = partition(nums, low, high)
        quick(nums, low, p-1)           #注意，快排的结尾和开头，不包含p，这个值被用来做标记
        quick(nums, p+1, high)
    return nums

def partition(nums, low, high):
    i = low-1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i],nums[j] = nums[j],nums[i] 
    nums[i+1],nums[high] = nums[high],nums[i+1]
    return i+1
# O(n2)
def insert(nums):
    for i in range(len(nums)):
        pre = i-1
        cur = nums[i]
        while pre>=0 and nums[pre] > cur:
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

# 每一位数，他的索引idx，需要对比他后面的所有数，比他小的把位置给idx，比完后当前位交换到idx
# O(n2)
def select(nums):
    for i in range(len(nums)):
        mid_idx = i
        for j in range(i+1,len(nums)):#这里从i的下一个开始
            if nums[mid_idx] > nums[j]:
                mid_idx = j
        nums[mid_idx],nums[i] = nums[i],nums[mid_idx] #这里是用I换
    return nums

# 插入排序的套路改版
# O(nlog2n)
def shell2(nums):
    n = len(nums)
    gap = n//2
    while gap > 0:
        for i in range(len(nums)):
            cur = nums[i]
            j = i
            while j-gap>=0 and nums[j-gap]>cur:
                nums[j] = nums[j-gap]
                j = j-gap
            nums[j] = cur
        gap //= 2
    return nums

# 视频讲解
# https://www.bilibili.com/video/av47196993?from=search&seid=8489142146697475476
# https://www.runoob.com/python3/python-heap-sort.html
def heapSort(arr): 
    def heapify(arr, n, i): 
        largest = i  
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
        if l < n and arr[i] < arr[l]: 
            largest = l 
        if r < n and arr[largest] < arr[r]: 
            largest = r 
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i]  # 交换
            heapify(arr, n, largest) 

    n = len(arr) 
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    # print(arr)
  
    # 一个个交换元素
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        heapify(arr, i, 0) 
    return arr

# 基数排序
# 从个位排，再十位排，再百位排，一直排到位数最长的那个
def radix_sort(s):
    i = 0                                               # 记录当前正在排拿一位，最低位为1
    max_num = max(s)                                    # 最大值
    j = len(str(max_num))                               # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)]            # 初始化桶数组
        for x in s:
            bucket_list[int(x / (10**i)) % 10].append(x)# 找到位置放入桶数组
        s.clear()
        # print(bucket_list)
        for x in bucket_list:                           # 放回原序列
            for y in x:
                s.append(y)
        # print(s)
        i += 1
    return s


arr = [10, 7, 8, 9, 1, 5, 5]
n = len(arr)
# re = bobble(arr)
# re = merge(arr)
# re = quick(arr, 0, n-1)
# re = insert(arr)--------
# re = bucket(arr)
# re = count(arr)-------
# re = select(arr)-------
# re = shell2(arr)
# re = heapSort(arr)
re = radix_sort(arr)
print(re)

