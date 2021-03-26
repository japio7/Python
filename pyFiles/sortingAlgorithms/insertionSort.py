import random

# Insertion sort
# a = 1 for acending
# a = -1 for decending
nums = []

# Generate nums with random numbers
for i in range(1, 11):
	a = random.randrange(1, 101)
	nums.append(a)
	
def insertionSort(nums, a = 1):
	for i in range(len(nums)):
		k = nums[i]
		j = i - 1
		if a == 1:
			while j >= 0 and k < nums[j]:
				nums[j+1] = nums[j]
				j-=1
			nums[j+1] = k
		elif a == -1:
			while j >= 0 and k > nums[j]:
				nums[j+1] = nums[j]
				j-=1
			nums[j+1] = k
		else:
			print("Invalid Argument Value!")
			return
	return nums

print(insertionSort(nums, 1))
print(insertionSort(nums, -1))
