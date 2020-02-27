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
        p = positive(nums, low, high)
        quick(nums, low, p-1)
        quick(nums, p+1, high)
    return nums

def positive(nums, low, high):
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
    max_len = max(nums)
    bucket = [0] * (max_len+1)
    for i in nums:
        bucket[i] += 1
    re = []
    for j in range(len(bucket)):
        if bucket[j] != 0:
            re.append(j)
    return re

def count(nums):
    re = [0]*len(nums)
    for i in range(len(nums)):
        p = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                p += 1
        re[p] = nums[i]
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

# def shell(nums):
#     n = len(nums)
#     gap = n//2
#     while gap > 0:
#         for i in range(len(nums)):
#             cur = nums[i]
#             j = i 
#             while j-gap>=0 and nums[j-gap]>cur:
#                 nums[j] = nums[j-gap]
#                 j = j-gap
#             nums[j] = cur
#         gap //= 2
#     return nums 

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


def min_heap_sort(input_list):
	
	def heap_adjust(input_list, parent, length):
		temp = input_list[parent]
		child=2 * parent + 1

		while child < length:
			if child+1 < length and input_list[child+1] < input_list[child]:
				child += 1
			if temp <= input_list[child]:
				break
			input_list[parent] = input_list[child]
			parent = child
			child = 2 * parent + 1
		input_list[parent] = temp

	sorted_list = input_list
	length = len(sorted_list)

	# 初始化堆
	for i in range(0, length // 2 + 1)[::-1]:
		heap_adjust(sorted_list, i, length)

	# 
	for j in range(1, length)[::-1]:
		sorted_list[j],sorted_list[0]=sorted_list[0],sorted_list[j]

		heap_adjust(sorted_list, 0, j)
		print('第%d趟排序:' % (length - j), end = '')
		print(sorted_list)

	return sorted_list

if __name__ == '__main__':
	input_list = [6, 4, 8, 9, 2, 3, 1]
	print('排序前:', input_list)
	sorted_list = min_heap_sort(input_list)
	print('排序后:', sorted_list)








arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
# re = bobble(arr)
# re = bucket(arr)
# re = count(arr)
# re = insert(arr)
re = merge(arr)
# re = quick(arr, 0, n-1)
# re = select(arr)
# re = shell2(arr)
print(re)
