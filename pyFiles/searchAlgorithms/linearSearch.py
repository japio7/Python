import random

nums = []

# Generate nums with random numbers
for i in range(1, 101):
	a = random.randrange(1, 51)
	nums.append(a)

# Generate random number to search for
r = random.randrange(1, 51)

# linear search
# While loop
def linearSearch_while(nums, n):
	i = 0
	while i < len(nums):
		if nums[i] == n:
			print(f"{n} found at index {i}")
			return True
		i+=1
		
	print(f"{n} does not exist in list!")
	return False

linearSearch_while(nums, r)

nums = []

# Generate nums with random numbers
for i in range(1, 101):
	a = random.randrange(1, 51)
	nums.append(a)

# Generate random number to search for
r = random.randrange(1, 51)

# Linear search
# For loop
def linearSearch_for(nums, n):
	for i in range(len(nums)):
		if nums[i]  == n:
			print(f"{n} found at index {i}")
			return True
		
	print(f"{n} does not exist in list!")
	return False

linearSearch_for(nums, r)
