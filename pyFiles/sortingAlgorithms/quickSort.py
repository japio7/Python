import random

# Merge sort
# a = 1 for acending
# a = -1 for decending
nums = []

# Generate nums with random numbers
for i in range(1, 11):
	a = random.randrange(1, 101)
	nums.append(a)
	
def mergeSort(nums, a = 1):
	if len(nums) > 1:
		mid = len(nums)//2
		left = nums[:mid]
		right = nums[mid:]
		mergeSort(left)
		mergeSort(right)
		
		i = j = k = 0
		
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
			
		if a == 1:
			return nums
		elif a == -1:
			nums.reverse()
			return nums
		else:
			print("Invalid Argument Value!")
			return
		
print(mergeSort(nums, 1))
print(mergeSort(nums, -1))
