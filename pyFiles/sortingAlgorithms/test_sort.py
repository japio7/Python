
import random
import pandas as pd
from time import time

def randomList(n):
	A = [i for i in range(n)]
	random.shuffle(A)
	return A

# Merge Sort
def mergeSort(nums):
	if len(nums) > 1:
		mid = len(nums)//2
		left = nums[:mid]
		right = nums[mid:]
		mergeSort(left)
		mergeSort(right)
		
		i, j, k = 0, 0, 0
		
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				nums[k] = left[i]
				i+=1
			else:
				nums[k] = right[j]
				j+=1
			k+=1
			
		while i < len(left):
			nums[k] = left[i]
			i+=1
			k+=1
			
		while j < len(right):
			nums[k] = right[j]
			j+=1
			k+=1
			
		return nums
	
# Insertion Sort
def insertionSort(nums):
	for i in range(len(nums)):
		k = nums[i]
		j = i - 1
		
		while j >= 0 and k < nums[j]:
			nums[j+1] = nums[j]
			j-=1
		nums[j+1] = k
		
	return nums

# Bubble Sort
def bubbleSort(nums):
	for i in range(len(nums)-1,0,-1):
		for j in range(i):
			if nums[j] > nums[j+1]:
				temp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = temp
				
	return nums

# Heap Sort
def heapSort(nums):
	length = len(nums) - 1
	leastParent = length//2
	
	for i in range(leastParent, -1, -1):
		moveDown(nums, i, length)
		
	for i in range(length, 0, -1):
		if nums[0] > nums[i]:
			swap(nums, 0, i)
			moveDown(nums, 0, i-1)
	return nums

def moveDown(a, F, L):
	largest = 2 * F + 1
	
	while largest <= L:
		if largest < L and a[largest] < a[largest+1]:
			largest+=1
		if a[largest] > a[F]:
			swap(a, largest, F)
			F = largest
			largest = 2 * F + 1
		else:
			return
		
def swap(A, x, y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp
	
# Quick Sort
def quickSort(nums):
	if len(nums) < 2:
		return nums
	
	partitionsPosition = 0 
	
	for i in range(1, len(nums)):
		if nums[i] <= nums[0]:
			partitionsPosition += 1
			temp = nums[i]
			nums[i] = nums[partitionsPosition]
			nums[partitionsPosition] = temp
			
	temp = nums[0]
	nums[0] = nums[partitionsPosition] 
	nums[partitionsPosition] = temp
	
	left = quickSort(nums[0:partitionsPosition])
	right = quickSort(nums[partitionsPosition+1:len(nums)])
	nums = left + [nums[partitionsPosition]] + right
	
	return nums

# Selection Sort
def selectionSort(nums, a = 1):
	for i in range(len(nums)-1):
		minPos = i
		for j in range(i, len(nums)):
			if nums[j] < nums[minPos]:
				minPos = j
				
		temp = nums[i]
		nums[i] = nums[minPos]
		nums[minPos] = temp
	return nums

def runTests(start, end, increment):
	a2 = []
	for n in range(start, end+1, increment):
		a1 = []
		lst = randomList(n)
		mergeCopy = lst.copy()
		insertCopy = lst.copy()
		bubbleCopy = lst.copy()
		heapCopy = lst.copy()
		quickCopy = lst.copy()
		selectCopy = lst.copy()
		pythonSort = lst.copy()
		pythonSorted = lst.copy()
		
		m1 = time()
		mergeSort(mergeCopy)
		m2 = time()
		mtime = (m2 - m1) * 1000
		
		i1 = time()
		insertionSort(insertCopy)
		i2 = time()
		itime = (i2 - i1) * 1000
		
		b1 = time()
		bubbleSort(bubbleCopy)
		b2 = time()
		btime = (b2 - b1) * 1000
		
		h1 = time()
		heapSort(heapCopy)
		h2 = time()
		htime = (h2 - h1) * 1000
		
		q1 = time()
		quickSort(quickCopy)
		q2 = time()
		qtime = (q2 - q1) * 1000
		
		s1 = time()
		selectionSort(selectCopy)
		s2 = time()
		stime = (s2 - s1) * 1000
		
		a1.append(n)
		a1.append(round(mtime, 2))
		a1.append(round(itime, 2))
		a1.append(round(btime, 2))
		a1.append(round(htime, 2))
		a1.append(round(qtime, 2))
		a1.append(round(stime, 2))
		
		a2.append(a1)
		
	return a2

matrix = pd.DataFrame(runTests(100, 3000, 100), columns = ['N', 'Merge', 'Insert', 'Bubble', 'Heap', 'Quick', 'Selection'])

result = matrix.to_string(index = False)

# Print result in milliseconds
print(result)
