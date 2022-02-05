import math

def permute(n, r):
	# How many different orders are there when
	# items cannot be repeated and order matters
	top = math.factorial(n)
	bot = math.factorial(n-r)
	return int(math.factorial(n)/math.factorial(n-r))

def combo(n, r):
	# How many different combinations are there
	# when itemns cannot be repeated and order
	# does not matter
	top = math.factorial(n)
	bot = math.factorial(n-r)*math.factorial(r)
	return int(top/bot)

def isValid(a):
	if a.lower() == "y" or a.lower() == "yes" or a.lower() == "n" or a.lower() == "no":
		return True
	return False

def main():
	n = input("Number of total items:\t")
	while not n.isdigit():
		n = input("Number of total items:\t")
		
	r = input("Number of items to be used:\t")
	while not r.isdigit():
		r = input("Number of items to be used:\t")
		
	ordered = input("Does order matter?\t")
	while not isValid(ordered):
		ordered = input("Does order matter?\t")
		
	if ordered.lower() == "y" or ordered.lower() == "yes":
		print(permute(int(n), int(r)))
	else:
		print(combo(int(n), int(r)))

main()