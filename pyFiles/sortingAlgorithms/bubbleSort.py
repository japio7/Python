import random

# Bubble sort
# a = 1 for acending
# a = -1 for decending
nums = []

# Generate nums with random numbers
for i in range(1, 11):
	a = random.randrange(1, 101)
	nums.append(a)
	
def bubbleSort(nums, a = 1):
	for i in range(len(nums)-1,0,-1):
		for j in range(i):
			if a == 1:
				if nums[j] > nums[j+1]:
					temp = nums[j]
					nums[j] = nums[j+1]
					nums[j+1] = temp
			elif a == -1:
				if nums[j] < nums[j+1]:
					temp = nums[j]
					nums[j] = nums[j+1]
					nums[j+1] = temp
			elif a != -1 or a != 1:
				print("Invalid Parameter Value!")
				return
	return nums

print(bubbleSort(nums, ))
print(bubbleSort(nums, -1))
