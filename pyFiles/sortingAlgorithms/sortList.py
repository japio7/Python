import random

nums = []

# Generate nums with random numbers
for i in range(1, 11):
	a = random.randrange(1, 101)
	nums.append(a)
	
# a = 1 for acending
# a = -1 for decending
def sortList(nums, a = 1):
	y = True
	k = 1
	while k < len(nums)-1 and y:
		y = False
		for i in range(len(nums) - k):
			if nums[i] > nums[i + 1]:
				temp = nums[i]
				nums[i] = nums[i + 1]
				nums[i + 1] = temp
				y = True
	if a == 1:
		return nums
	elif a == -1:
		nums.reverse()
		return nums
	else:
		print("Invalid Argument Value!")
		return
	
print(sortList(nums, 1))
print(sortList(nums, -1))
