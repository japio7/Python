# Has to be a sorted list
# This algorithm automatically sorts the list

import random

nums = []

# Generate nums with random numbers
for i in range(1, 101):
	a = random.randrange(1, 51)
	nums.append(a)
	
# Binary search
inp = int(input("What number do you want to search for in the list between 1 and 50: "))

ind = 0

def find(fun, n):
	if fun == True:
		print(f"After sorted list, {n} found at index {ind}!")
	else:
		print(f"{n} not found!")

def binSearch(nums, n = inp):
	nums.sort()
	print(nums)
	low = 0
	up = len(nums)-1
	
	while low <= up:
		mid = (low + up) // 2
		if nums[mid] == n:
			globals()['ind'] = mid
			return True
		elif nums[mid] < n:
			low = mid + 1
		else:
			up = mid - 1
			
	return False

find(binSearch(nums), inp)
