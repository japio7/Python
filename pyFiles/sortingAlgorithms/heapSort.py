import random

# Heap sort
# a = 1 for acending
# a = -1 for decending
nums = []

# Generate nums with random numbers
for i in range(1, 11):
	a = random.randrange(1, 101)
	nums.append(a)
	
def heapSort(nums, a = 1):
	length = len(nums) - 1
	leastParent = length//2
	
	for i in range(leastParent, -1, -1):
		moveDown(nums, i, length)
		
	for i in range(length, 0, -1):
		if nums[0] > nums[i]:
			swap(nums, 0, i)
			moveDown(nums, 0, i-1)
			
	if a == 1:
		return nums
	elif a == -1:
		nums.reverse()
		return nums
	else:
		print("Invalid Argument Value!")
		return
	
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
	
print(heapSort(nums, 1))
print(heapSort(nums, -1))
