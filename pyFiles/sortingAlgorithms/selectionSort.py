import random

# Selection sort
# a = 1 for acending
# a = -1 for decending
nums = []

# Generate nums with random numbers
for i in range(1, 11):
	a = random.randrange(1, 101)
	nums.append(a)
	
def selectionSort(nums, a = 1):
	for i in range(len(nums)-1):
		minPos = i
		for j in range(i, len(nums)):
			if a == 1:
				if nums[j] < nums[minPos]:
					minPos = j
			elif a == -1:
				if nums[j] > nums[minPos]:
					minPos = j
			else:
				print("Invalid Argument Value!")
				return
			
		temp = nums[i]
		nums[i] = nums[minPos]
		nums[minPos] = temp
	return nums

print(selectionSort(nums, 1))
print(selectionSort(nums, -1))
